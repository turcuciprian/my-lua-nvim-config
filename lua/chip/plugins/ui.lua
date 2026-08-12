-- UI niceties: a statusline and a popup that shows available keybindings.
return {
  -- Statusline
  {
    "nvim-lualine/lualine.nvim",
    dependencies = { "nvim-tree/nvim-web-devicons" },
    config = function()
      -- VS Code Dark Modern status bar: flat #181818 with #CCCCCC text
      local dark_modern = {
        normal = {
          a = { fg = "#CCCCCC", bg = "#181818", gui = "bold" },
          b = { fg = "#CCCCCC", bg = "#181818" },
          c = { fg = "#CCCCCC", bg = "#181818" },
        },
        inactive = {
          a = { fg = "#9D9D9D", bg = "#181818" },
          b = { fg = "#9D9D9D", bg = "#181818" },
          c = { fg = "#9D9D9D", bg = "#181818" },
        },
      }
      -- Every mode looks the same, like the real VS Code status bar
      dark_modern.insert = dark_modern.normal
      dark_modern.visual = dark_modern.normal
      dark_modern.replace = dark_modern.normal
      dark_modern.command = dark_modern.normal
      dark_modern.terminal = dark_modern.normal

      require("lualine").setup({
        options = { theme = dark_modern, globalstatus = true },
      })
    end,
  },

  -- which-key: press <leader> and wait to see every available mapping
  {
    "folke/which-key.nvim",
    event = "VeryLazy",
    config = function()
      local wk = require("which-key")
      wk.setup({})
      wk.add({
        { "<leader>p", group = "project / paste" },
        { "<leader>f", group = "find (telescope)" },
        { "<leader>s", group = "search & replace" },
        { "<leader>g", group = "git" },
        { "<leader>h", group = "git hunks / harpoon" },
        { "<leader>c", group = "code (lsp)" },
        { "<leader>b", group = "buffers" },
      })
    end,
  },
}
