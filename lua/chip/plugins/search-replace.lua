-- grug-far: project-wide search & replace with a live preview buffer.
-- Powered by ripgrep; edit the search/replace fields, see every match, and
-- apply across the whole project at once.
return {
  "MagicDuck/grug-far.nvim",
  config = function()
    require("grug-far").setup({})
  end,
  keys = {
    {
      "<leader>sr",
      function() require("grug-far").open() end,
      desc = "Search & Replace (project-wide)",
    },
    {
      "<leader>sw",
      function() require("grug-far").open({ prefills = { search = vim.fn.expand("<cword>") } }) end,
      desc = "Search & Replace word under cursor",
    },
    {
      "<leader>sf",
      function() require("grug-far").open({ prefills = { paths = vim.fn.expand("%") } }) end,
      desc = "Search & Replace in current file",
    },
  },
}
