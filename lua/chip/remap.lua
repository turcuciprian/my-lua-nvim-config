-- Leader must be set before lazy.nvim loads (so plugin <leader> maps register correctly)
vim.g.mapleader = " "
vim.g.maplocalleader = " "

local map = vim.keymap.set

-- Built-in netrw file explorer (kept from the original config)
map("n", "<leader>pv", vim.cmd.Ex, { desc = "Open netrw file explorer" })

-- Move visual selection up/down, re-indenting as it goes
map("v", "J", ":m '>+1<CR>gv=gv", { desc = "Move selection down" })
map("v", "K", ":m '<-2<CR>gv=gv", { desc = "Move selection up" })

-- Keep the cursor centred while scrolling / searching
map("n", "<C-d>", "<C-d>zz")
map("n", "<C-u>", "<C-u>zz")
map("n", "n", "nzzzv")
map("n", "N", "Nzzzv")

-- Paste over a selection without clobbering the yank register
map("x", "<leader>p", [["_dP]], { desc = "Paste without yanking selection" })
-- Delete to the black-hole register (does not touch the clipboard)
map({ "n", "v" }, "<leader>D", [["_d]], { desc = "Delete to void register" })
-- Explicit yank to system clipboard
map({ "n", "v" }, "<leader>y", [["+y]], { desc = "Yank to system clipboard" })

-- Substitute the word under the cursor across the current file
map("n", "<leader>S", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]],
  { desc = "Substitute word under cursor (this file)" })

-- Window navigation
map("n", "<C-h>", "<C-w>h", { desc = "Window left" })
map("n", "<C-j>", "<C-w>j", { desc = "Window down" })
map("n", "<C-k>", "<C-w>k", { desc = "Window up" })
map("n", "<C-l>", "<C-w>l", { desc = "Window right" })

-- Buffers
map("n", "<leader>bn", "<cmd>bnext<cr>", { desc = "Next buffer" })
map("n", "<leader>bp", "<cmd>bprevious<cr>", { desc = "Previous buffer" })
map("n", "<leader>bd", "<cmd>bdelete<cr>", { desc = "Delete buffer" })

-- Clear search highlight
map("n", "<leader>nh", "<cmd>nohlsearch<cr>", { desc = "Clear search highlight" })
map('n', '<leader>l', vim.diagnostic.open_float, { desc = 'Show line diagnostics' })
