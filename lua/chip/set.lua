-- Editor options
local opt = vim.opt

opt.nu = true                 -- absolute line number on current line
opt.relativenumber = true     -- relative numbers elsewhere (fast j/k motions)
opt.cursorline = true
opt.cursorcolumn = true

-- Indentation
opt.tabstop = 2
opt.softtabstop = 2
opt.shiftwidth = 2
opt.expandtab = true
opt.smartindent = true

-- Search
opt.ignorecase = true         -- (vim.opt.ic) case-insensitive...
opt.smartcase = true          -- ...unless the query has a capital letter
opt.hlsearch = false
opt.incsearch = true

-- UI / behaviour
opt.wrap = false
opt.scrolloff = 8
opt.signcolumn = "yes"
opt.termguicolors = true
opt.updatetime = 50
opt.splitright = true
opt.splitbelow = true
opt.clipboard = "unnamedplus" -- yank/paste use the system clipboard

-- Persistent undo (survives quitting nvim), no swap/backup clutter
opt.swapfile = false
opt.backup = false
opt.undofile = true
opt.undodir = vim.fn.stdpath("data") .. "/undodir"

opt.isfname:append("@-@")
