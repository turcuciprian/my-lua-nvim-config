-- nvim-tree: a persistent sidebar file explorer
return {
  "nvim-tree/nvim-tree.lua",
  dependencies = { "nvim-tree/nvim-web-devicons" },
  config = function()
    require("nvim-tree").setup({
      view = { width = 35 },
      renderer = { group_empty = true },
      filters = { dotfiles = false },
      git = { enable = true },
    })
    vim.keymap.set("n", "<leader>e", "<cmd>NvimTreeToggle<cr>", { desc = "Explorer: toggle" })
    vim.keymap.set("n", "<leader>E", "<cmd>NvimTreeFindFile<cr>", { desc = "Explorer: reveal current file" })
  end,
}
