-- Small editing-quality plugins
return {
  -- Surround text objects: cs"' ds( ysiw) etc.
  { "tpope/vim-surround" },

  -- Auto-close brackets / quotes
  {
    "windwp/nvim-autopairs",
    event = "InsertEnter",
    config = true,
  },
}
