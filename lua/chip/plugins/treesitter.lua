-- Treesitter: accurate syntax highlighting & indentation
return {
  "nvim-treesitter/nvim-treesitter",
  branch = "master", -- classic `.configs` API (stable)
  build = ":TSUpdate",
  config = function()
    require("nvim-treesitter.configs").setup({
      ensure_installed = {
        "c", "lua", "vim", "vimdoc", "query",
        "markdown", "markdown_inline", "python",
        "javascript", "typescript", "tsx",
        "json", "yaml", "toml", "bash",
        "html", "css", "dart",
      },
      sync_install = false,
      auto_install = true,
      highlight = { enable = true, additional_vim_regex_highlighting = false },
      indent = { enable = true },
    })
  end,
}
