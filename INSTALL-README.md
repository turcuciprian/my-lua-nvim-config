# INSTALL-README

A step-by-step guide to reproduce the Neovim setup **exactly as it is installed
and configured on this machine right now**.

> ⚠️ **Important note about this repository.**
> The files committed in *this* repo are an older, **packer.nvim**-based config
> (see `README.md`, `lua/`, `instances/`, `custom_library/`). The configuration
> that is actually live on the system is a newer **lazy.nvim**-based config that
> lives in `~/.config/nvim` under the `chip` namespace. This document describes
> the **live system setup** so it can be rebuilt from scratch. Where it matters,
> the relevant config files are reproduced inline below.

---

## 1. System snapshot (what is installed today)

| Component        | Value on this machine                                  |
| ---------------- | ------------------------------------------------------- |
| OS               | macOS 26.5.1 (build 25F80)                               |
| Architecture     | Apple Silicon (`arm64`)                                  |
| Package manager  | Homebrew, installed at `/opt/homebrew`                   |
| Neovim           | **0.12.2** (`/opt/homebrew/Cellar/neovim/0.12.2`)       |
| Plugin manager   | **lazy.nvim** (self-bootstrapping, pinned via lockfile) |
| Config location  | `~/.config/nvim`                                         |
| Config namespace | `chip` (i.e. `~/.config/nvim/lua/chip/...`)             |

### External tools the config depends on

These are required by various plugins. Versions are what is present today:

| Tool          | Used by                                            | Status on this machine             |
| ------------- | -------------------------------------------------- | ---------------------------------- |
| `git`         | lazy.nvim, telescope git pickers, fugitive, neogit | 2.50.1 (Apple Git) ✅               |
| `ripgrep` (`rg`) | telescope live-grep, grug-far search & replace  | 14.1.1 ✅                           |
| C compiler    | telescope-fzf-native, treesitter parser builds     | Apple clang 21 (Xcode CLT) ✅        |
| `make`        | building `telescope-fzf-native` (`build = "make"`) | GNU Make 3.81 ✅                     |
| `python3`     | pyright / general Python LSP work                  | 3.9.6 (system) ✅                   |
| `node` + `npm`| **required** to run several Mason LSP servers      | ⚠️ install these (see step 3)       |
| `fd`          | (optional) faster file finding in telescope        | ⚠️ optional, recommended           |

> The TypeScript/JavaScript, Bash, JSON, HTML and CSS language servers installed
> through Mason are Node packages. They will not start unless `node`/`npm` are on
> the `PATH`, so install Node even though Neovim itself does not need it.

---

## 2. Install Neovim + system dependencies (Homebrew)

If Homebrew is not present yet, install it first:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then install Neovim and the supporting tools to match this machine:

```bash
# Core editor
brew install neovim          # currently 0.12.2

# Plugin dependencies
brew install ripgrep         # rg  -> telescope live-grep + grug-far
brew install fd              # optional, faster file finder
brew install node            # node + npm -> runtime for several LSP servers
```

A C compiler and `make` are needed to build `telescope-fzf-native` and the
Treesitter parsers. On macOS these come from the Xcode Command Line Tools:

```bash
xcode-select --install   # provides clang + make (safe to run if already installed)
```

Verify:

```bash
nvim --version           # expect NVIM v0.12.x
rg --version && node --version && cc --version && make --version
```

---

## 3. Install the configuration

The live config is a small, modular lazy.nvim setup. Recreate it under
`~/.config/nvim`.

```bash
mkdir -p ~/.config/nvim/lua/chip/plugins
```

### 3.1 Entry point — `~/.config/nvim/init.lua`

```lua
require("chip")
```

### 3.2 Module loader — `~/.config/nvim/lua/chip/init.lua`

```lua
-- Load order matters: set leader + core remaps before lazy bootstraps plugins.
require("chip.set")
require("chip.remap")
require("chip.lazy")
```

### 3.3 The rest of the config

The remaining files live in `~/.config/nvim/lua/chip/`:

```
lua/chip/
├── init.lua            -- requires set / remap / lazy (above)
├── set.lua             -- editor options (numbers, indent, undofile, clipboard…)
├── remap.lua           -- leader = <Space> + core keymaps
├── lazy.lua            -- bootstraps lazy.nvim, imports lua/chip/plugins/
└── plugins/            -- one spec file per concern, auto-imported by lazy
    ├── colorscheme.lua     -- rose-pine (transparent bg)
    ├── editing.lua         -- vim-surround, nvim-autopairs
    ├── git.lua             -- gitsigns, diffview, neogit, fugitive
    ├── harpoon.lua         -- harpoon2 file pinning
    ├── lsp.lua             -- mason + lspconfig + nvim-cmp + LuaSnip
    ├── nvim-tree.lua       -- file-explorer sidebar
    ├── search-replace.lua  -- grug-far project search & replace
    ├── telescope.lua       -- fuzzy finder (+ fzf-native, built with make)
    ├── treesitter.lua      -- syntax highlighting / indentation
    ├── ui.lua              -- lualine statusline + which-key
    └── undotree.lua        -- undo history viewer
```

`lazy.lua` bootstraps the plugin manager and imports every spec under
`lua/chip/plugins/` automatically:

```lua
-- Bootstrap lazy.nvim (the plugin manager) if it is not already present
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not (vim.uv or vim.loop).fs_stat(lazypath) then
  vim.fn.system({
    "git", "clone", "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

require("lazy").setup("chip.plugins", {
  change_detection = { notify = false },
})
```

> Because lazy.nvim is self-bootstrapping, you do **not** install a plugin
> manager by hand (unlike the old packer-based `README.md` in this repo). It is
> cloned automatically on first launch.

### 3.4 Pin plugin versions (optional but recommended)

The exact plugin commits running on this machine are recorded in
`~/.config/nvim/lazy-lock.json`. Copy that file into place to reproduce the same
versions, then run `:Lazy restore` inside Neovim to check them out.

---

## 4. First launch — what happens automatically

Open Neovim:

```bash
nvim
```

On first start, in order:

1. **lazy.nvim** clones itself, then installs all plugins listed under
   `lua/chip/plugins/`.
2. **telescope-fzf-native** is compiled (`make`) — needs the C compiler.
3. **Mason** installs the language servers declared in `lsp.lua`
   (`ensure_installed`). The servers present on this machine are:
   - `lua_ls`  (lua-language-server)
   - `pyright`
   - `ts_ls`   (typescript-language-server) — needs Node
   - `bashls`  (bash-language-server) — needs Node
   - `jsonls`  (json-lsp) — needs Node
   - `html`    (html-lsp) — needs Node
   - `cssls`   (css-lsp) — needs Node
4. **Treesitter** installs/compiles parsers (`:TSUpdate`). Parsers configured:
   `c, lua, vim, vimdoc, query, markdown, markdown_inline, python, javascript,
   typescript, tsx, json, yaml, toml, bash, html, css, dart`.

Useful commands to drive / verify the install:

```vim
:Lazy        " plugin manager dashboard (install / update / restore)
:Mason       " language-server installer UI
:checkhealth " diagnose missing external dependencies
:TSUpdate    " (re)build treesitter parsers
```

Let everything finish, then **restart Neovim** so all plugins load cleanly.

---

## 5. Verifying the install matches this machine

After the first launch settles:

```bash
# Mason-installed language servers should be:
ls ~/.local/share/nvim/mason/packages
#   bash-language-server  css-lsp  html-lsp  json-lsp
#   lua-language-server   pyright  typescript-language-server

# Treesitter parsers compiled here:
ls ~/.local/share/nvim/lazy/nvim-treesitter/parser
```

Inside Neovim, `:checkhealth` should report `git`, `rg`, a C compiler, and
`node` as found. If `node` is missing, the Node-based LSP servers above will be
listed as failing to start — install Node (step 2) and restart.

---

## 6. Quick reference: key settings baked into the config

- **Leader key**: `<Space>` (set in `remap.lua` before plugins load).
- **Indentation**: 2 spaces, `expandtab`, `smartindent`.
- **Line numbers**: absolute + relative (`nu` + `relativenumber`).
- **Clipboard**: `unnamedplus` (yank/paste use the system clipboard).
- **Persistent undo**: enabled, stored in `stdpath("data")/undodir`;
  no swap/backup files.
- **Colorscheme**: `rose-pine` with a transparent background.

For the day-to-day keybindings and workflow, see
[`USAGE-README.MD`](./USAGE-README.MD).
