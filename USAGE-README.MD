# Neovim — Usage & Keybinding Guide

Your personal Neovim setup, installed on **2026-06-07**.

- **Config location:** `~/.config/nvim/`  (Lua, organised under `lua/chip/`)
- **Plugin manager:** [lazy.nvim](https://github.com/folke/lazy.nvim)
- **Leader key:** `<Space>` — wherever you see `<leader>` below, press **Space**.
- This is a modernised superset of your old `my-lua-nvim-config` (Packer → lazy.nvim),
  with everything you had **plus** a full git diff visualiser, project-wide
  search & replace, a popup keybinding helper, a statusline, and more LSP servers.

> **Tip:** Press `<Space>` and pause — the **which-key** popup lists every
> mapping available. You rarely need to memorise anything.

---

## 0. Notation cheatsheet

| Symbol | Means |
|--------|-------|
| `<leader>` | the **Space** bar |
| `<C-x>` | hold **Ctrl** and press `x` |
| `<S-x>` | hold **Shift** and press `x` (often shown as a capital letter) |
| `<CR>` | the **Enter / Return** key |
| `<F2>` etc. | the function keys |
| "normal mode" | the default mode (press `<Esc>` to get there) |
| "insert mode" | typing text (press `i` / `a` to enter) |
| "visual mode" | selecting text (press `v` / `V`) |

---

## 1. First things to know (Vim basics)

| Key | Action |
|-----|--------|
| `i` / `a` | Insert before / after cursor |
| `<Esc>` | Back to normal mode |
| `:w` `<CR>` | Save file |
| `:q` `<CR>` | Quit (`:q!` = quit without saving) |
| `:wq` / `ZZ` | Save and quit |
| `h j k l` | Move left / down / up / right |
| `w` / `b` | Next / previous word |
| `0` / `$` | Start / end of line |
| `gg` / `G` | Top / bottom of file |
| `dd` / `yy` / `p` | Delete line / yank (copy) line / paste |
| `u` / `<C-r>` | Undo / redo |
| `/text` `<CR>` | Search forward (`n` next, `N` previous) |
| `:%s/old/new/g` | Replace in current file (built-in) |

Line numbers are **relative**, so `5j` jumps 5 lines down, `12k` jumps 12 up.

---

## 2. File & project navigation

### Telescope (fuzzy finder)
| Key | Action |
|-----|--------|
| `<leader>pf` / `<leader>ff` | **Find files** in project (fuzzy) |
| `<leader>pg` / `<C-p>` | Find **git-tracked** files |
| `<leader>fo` | Recently opened files |
| `<leader>fb` | Switch between **open buffers** |
| `<leader>fh` | Search Neovim **help** |
| `<leader>fr` | **Resume** the last Telescope search |
| `<leader>fd` | List all **diagnostics** (errors/warnings) in project |

Inside any Telescope window: type to filter, `<C-n>`/`<C-p>` or `<C-j>`/`<C-k>`
to move, `<CR>` to open, `<C-x>` open in split, `<C-v>` open in vsplit,
`<C-t>` open in new tab, `<Esc>` to close.

### File explorers
| Key | Action |
|-----|--------|
| `<leader>e` | Toggle the **nvim-tree** sidebar |
| `<leader>E` | Reveal the current file in the sidebar |
| `<leader>pv` | Open the built-in netrw explorer (old habit, still here) |

Inside nvim-tree: `<CR>` open, `a` create, `d` delete, `r` rename, `x` cut,
`c` copy, `p` paste, `R` refresh, `H` toggle hidden files, `q` close, `g?` help.

### Harpoon (instant jump between your few key files)
| Key | Action |
|-----|--------|
| `<leader>a` | **Add** current file to the harpoon list |
| `<C-e>` | Toggle the harpoon **quick menu** |
| `<leader>1` … `<leader>4` | Jump straight to harpooned file 1–4 |
| `<leader>hn` / `<leader>hP` | Next / previous harpoon mark |

### Windows & buffers
| Key | Action |
|-----|--------|
| `<C-h>` `<C-j>` `<C-k>` `<C-l>` | Move to window left/down/up/right |
| `:vsplit` / `:split` | Split window vertically / horizontally |
| `<leader>bn` / `<leader>bp` | Next / previous buffer |
| `<leader>bd` | Close (delete) the current buffer |

---

## 3. Searching the whole project

| Key | Action |
|-----|--------|
| `<leader>fg` | **Live grep** — type and see matches across the project live |
| `<leader>fw` | Grep the **word under the cursor** project-wide |
| `<leader>ps` | Prompt for a string, then grep the project for it |

These use `ripgrep` under the hood, so they are fast and respect `.gitignore`.

---

## 4. Search & replace

### In the current file (built-in)
| Key / Command | Action |
|---------------|--------|
| `<leader>S` | Replace the **word under the cursor** throughout this file (cursor lands ready to type the replacement) |
| `:%s/old/new/g` | Replace `old` → `new` everywhere in this file |
| `:%s/old/new/gc` | …same, but **confirm** each one (`y`/`n`/`a`/`q`) |

### Project-wide (grug-far)
| Key | Action |
|-----|--------|
| `<leader>sr` | Open **grug-far**: project-wide search & replace with live preview |
| `<leader>sw` | Same, pre-filled with the **word under the cursor** |
| `<leader>sf` | Same, but limited to the **current file** |

**How grug-far works:** a buffer opens with fields for *Search*, *Replace*,
*Files Filter*, and *Flags*. Type in each field; every match in the project
appears below as you type. Then:

| Key (inside grug-far) | Action |
|-----------------------|--------|
| `<leader>r` | **Replace all** matches |
| `<leader>l` | List / focus the results |
| `<CR>` | Jump to the match under the cursor (in its real file) |
| `<leader>s` | Sync the changes you typed back to the files |
| `<leader>x` (on a line) | Discard that one match from the replacement |
| `<leader>q` | Send results to the quickfix list |
| `g?` | Show grug-far's own help |

---

## 5. Autocomplete & code intelligence (LSP)

Completion (**nvim-cmp**) pops up automatically as you type in insert mode.
Language servers are auto-installed via **Mason** — currently:
Lua, Python (pyright), TypeScript/JavaScript, Bash, JSON, HTML, CSS.
(More install automatically the first time you open a matching file.)

### Completion menu — insert mode
| Key | Action |
|-----|--------|
| `<C-Space>` | Manually trigger the completion menu |
| `<C-n>` / `<C-p>` | Next / previous suggestion |
| `<Tab>` / `<S-Tab>` | Next / previous suggestion (and jump snippet fields) |
| `<CR>` | Accept the selected suggestion |
| `<C-b>` / `<C-f>` | Scroll the documentation popup up / down |
| `<C-e>` | Close the completion menu |

### Code actions — normal mode (active when a language server is attached)
| Key | Action |
|-----|--------|
| `K` | Show **hover** documentation for the symbol |
| `gd` | **Go to definition** |
| `gD` | Go to declaration |
| `gi` | Go to implementation |
| `go` | Go to type definition |
| `gr` | Find **all references** (in Telescope) |
| `gs` | Show function **signature** help |
| `<leader>rn` or `<F2>` | **Rename** the symbol everywhere |
| `<leader>ca` or `<F4>` | **Code action** (quick fixes, imports, …) |
| `<leader>cf` or `<F3>` | **Format** the file (or selection) |
| `<leader>cd` | Show the diagnostic message for the current line |
| `]d` / `[d` | Jump to next / previous diagnostic (error/warning) |

### Managing language servers
- `:Mason` — open the Mason UI: `i` to install, `X` to uninstall, `u` to update.
- `:LspInfo` — show which servers are attached to the current buffer.

---

## 6. Git

You have four complementary git tools. Day to day you'll mostly use
**gitsigns** (inline) and **diffview** (visual diffs).

### Inline changes — gitsigns
Changed lines are marked in the left gutter. With the cursor in a file:

| Key | Action |
|-----|--------|
| `]c` / `[c` | Jump to next / previous changed **hunk** |
| `<leader>hp` | **Preview** the hunk under the cursor |
| `<leader>hs` | **Stage** the hunk (in visual mode: stage selected lines) |
| `<leader>hr` | **Reset** the hunk (discard changes) |
| `<leader>hS` | Stage the whole file |
| `<leader>hR` | Reset the whole file |
| `<leader>hd` | Diff the current file against the index |
| `<leader>hb` / `<leader>gb` | **Blame** the current line (who/when/why) |
| `<leader>ht` | Toggle persistent inline blame for every line |

### Visual diff & history — diffview (the main diff visualiser)
| Key | Action |
|-----|--------|
| `<leader>gd` | **Open Diffview** — side-by-side diff of all working-tree changes |
| `<leader>gc` | **Close** Diffview |
| `<leader>gh` | **File history** of the *current* file (browse every past version) |
| `<leader>gH` | File history of the whole **branch / repo** |
| `<leader>gm` | Diff your branch against `main` (`origin/HEAD...HEAD`) |

Inside Diffview: the left panel lists changed files.
`<Tab>` / `<S-Tab>` cycle files, `<CR>` opens the diff, `j`/`k` move in the
list, `-` stage/unstage a file, `g?` shows help, `:DiffviewClose` or
`<leader>gc` exits. In a file-history view, `<CR>` on a commit shows that
commit's diff.

### Full git UI — neogit (stage, commit, branch, push, pull)
| Key | Action |
|-----|--------|
| `<leader>gg` | Open the **Neogit** dashboard |

Inside Neogit: `<Tab>` expand/collapse a section, `s` stage, `u` unstage,
`c` then `c` to **commit** (write message, then `<C-c><C-c>` to confirm),
`P` push, `F` (or `p`) pull, `b` branch menu, `l` log menu, `x` discard,
`$` show git output, `q` quit, `?` help.

### Raw git commands — fugitive
| Key / Command | Action |
|---------------|--------|
| `<leader>gs` | `:Git` status window (stage with `s`, unstage `u`, commit `cc`) |
| `:Git <anything>` | Run any git command, e.g. `:Git push`, `:Git log`, `:Git blame` |
| `:Git blame` | Full-file blame in a side column |

### Git via Telescope
| Key | Action |
|-----|--------|
| `<leader>gl` | Browse git **commits** (log) — `<CR>` checks one out |
| `<leader>gB` | Browse and switch git **branches** |

---

## 7. Undo history — undotree

| Key | Action |
|-----|--------|
| `<leader>u` | Toggle the **Undotree** panel |

Undo is **persistent** — it survives quitting Neovim. In the Undotree panel,
move with `j`/`k` to time-travel through every past state of the file.

---

## 8. Editing helpers

### Surround (vim-surround)
| Key | Action |
|-----|--------|
| `cs"'` | **Change** surrounding `"` to `'` |
| `ds"` | **Delete** surrounding `"` |
| `ysiw)` | **Add** `(` `)` around the inner word |
| `S)` (in visual mode) | Surround the selection with `(` `)` |

### Comments (built-in)
| Key | Action |
|-----|--------|
| `gcc` | Toggle comment on the current line |
| `gc` (visual) | Toggle comment on the selection |
| `gcap` | Toggle comment on a paragraph |

### Handy custom maps
| Key | Action |
|-----|--------|
| `J` / `K` (visual mode) | Move the selected lines down / up |
| `<leader>p` (visual mode) | Paste over selection **without** losing your copied text |
| `<leader>y` | Yank to the system clipboard explicitly |
| `<leader>D` | Delete without overwriting the clipboard |
| `<leader>nh` | Clear search highlighting |
| `<C-d>` / `<C-u>` | Half-page down / up (cursor stays centred) |
| `n` / `N` | Next / previous search result (centred on screen) |
| Auto-pairs | Typing `(`, `[`, `{`, `"` auto-inserts the closing pair |

---

## 9. Managing the setup itself

| Command | Action |
|---------|--------|
| `:Lazy` | Plugin manager UI — `S` sync, `U` update, `C` clean, `x` clear, `?` help |
| `:Lazy update` | Update all plugins |
| `:Mason` | Install / manage language servers, formatters, linters |
| `:checkhealth` | Diagnose problems with Neovim or any plugin |
| `:Telescope keymaps` | Search **every** keybinding currently active |

### Where things live
```
~/.config/nvim/
├── init.lua                 # entry point  -> require("chip")
└── lua/chip/
    ├── init.lua             # loads set, remap, lazy
    ├── set.lua              # editor options
    ├── remap.lua            # core (non-plugin) keymaps
    ├── lazy.lua             # bootstraps lazy.nvim + imports plugins/
    └── plugins/             # one file per topic (each returns a lazy spec)
        ├── colorscheme.lua  # rose-pine
        ├── telescope.lua    # fuzzy find + project grep
        ├── treesitter.lua   # syntax highlighting
        ├── harpoon.lua      # quick file jumps
        ├── undotree.lua     # undo history
        ├── editing.lua      # surround + autopairs
        ├── nvim-tree.lua    # file explorer sidebar
        ├── git.lua          # gitsigns + diffview + neogit + fugitive
        ├── search-replace.lua # grug-far (project-wide replace)
        ├── lsp.lua          # language servers + autocomplete
        └── ui.lua           # lualine statusline + which-key
```

To add a plugin: drop a new `.lua` file in `plugins/` that returns a lazy
spec, save, and run `:Lazy sync`.

---

## 10. Quick reference — the 20 you'll use most

| Key | Does |
|-----|------|
| `<Space>` (wait) | Show all keybindings (which-key) |
| `<leader>pf` | Find a file |
| `<leader>fg` | Search text across the project |
| `<leader>sr` | Search & replace across the project |
| `<leader>e` | Toggle file explorer |
| `<leader>a` / `<C-e>` | Harpoon: add file / open menu |
| `<leader>1`–`4` | Jump to harpooned file |
| `gd` / `gr` / `K` | Definition / references / hover docs |
| `<leader>rn` / `<leader>ca` | Rename / code action |
| `<leader>cf` | Format file |
| `]d` / `[d` | Next / previous error |
| `<leader>gd` | Open visual git diff |
| `<leader>gg` | Open git UI (Neogit) |
| `<leader>hp` / `<leader>hs` | Preview / stage a git hunk |
| `<leader>gb` | Blame current line |
| `<leader>u` | Undo-tree |
| `<leader>S` | Replace word under cursor (this file) |
| `<C-Space>` | Trigger autocomplete |
| `:w` / `:q` | Save / quit |

---

*Generated for `turcuciprian`. Edit any keybinding in
`~/.config/nvim/lua/chip/` and run `:Lazy sync` to apply changes.*
