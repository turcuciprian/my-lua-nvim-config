-- Undotree: visualise & browse the full undo history as a tree
return {
  "mbbill/undotree",
  config = function()
    vim.keymap.set("n", "<leader>u", vim.cmd.UndotreeToggle, { desc = "Undotree: toggle" })
  end,
}
