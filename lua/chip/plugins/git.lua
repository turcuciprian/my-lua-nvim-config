-- Git tooling: inline signs (gitsigns), a full-screen diff/history viewer
-- (diffview), a magit-style git UI (neogit), and fugitive for raw git commands.
return {
  -----------------------------------------------------------------------------
  -- gitsigns: signs in the gutter, hunk staging/preview/reset, inline blame
  -----------------------------------------------------------------------------
  {
    "lewis6991/gitsigns.nvim",
    event = { "BufReadPre", "BufNewFile" },
    config = function()
      require("gitsigns").setup({
        on_attach = function(bufnr)
          local gs = require("gitsigns")
          local function map(mode, l, r, desc)
            vim.keymap.set(mode, l, r, { buffer = bufnr, desc = desc })
          end

          -- Navigate between changed hunks
          map("n", "]c", function()
            if vim.wo.diff then vim.cmd.normal({ "]c", bang = true }) else gs.nav_hunk("next") end
          end, "Next git hunk")
          map("n", "[c", function()
            if vim.wo.diff then vim.cmd.normal({ "[c", bang = true }) else gs.nav_hunk("prev") end
          end, "Previous git hunk")

          -- Stage / reset / preview hunks
          map("n", "<leader>hs", gs.stage_hunk, "Stage hunk")
          map("n", "<leader>hr", gs.reset_hunk, "Reset hunk")
          map("v", "<leader>hs", function() gs.stage_hunk({ vim.fn.line("."), vim.fn.line("v") }) end, "Stage selected lines")
          map("v", "<leader>hr", function() gs.reset_hunk({ vim.fn.line("."), vim.fn.line("v") }) end, "Reset selected lines")
          map("n", "<leader>hS", gs.stage_buffer, "Stage whole buffer")
          map("n", "<leader>hR", gs.reset_buffer, "Reset whole buffer")
          map("n", "<leader>hp", gs.preview_hunk, "Preview hunk")
          map("n", "<leader>hd", gs.diffthis, "Diff this file")

          -- Blame
          map("n", "<leader>hb", function() gs.blame_line({ full = true }) end, "Blame current line")
          map("n", "<leader>gb", function() gs.blame_line({ full = true }) end, "Blame current line")
          map("n", "<leader>ht", gs.toggle_current_line_blame, "Toggle inline blame")
        end,
      })
    end,
  },

  -----------------------------------------------------------------------------
  -- diffview: the primary diff / merge / file-history visualiser
  -----------------------------------------------------------------------------
  {
    "sindrets/diffview.nvim",
    dependencies = { "nvim-lua/plenary.nvim" },
    config = function()
      require("diffview").setup({ enhanced_diff_hl = true })
    end,
    keys = {
      { "<leader>gd", "<cmd>DiffviewOpen<cr>", desc = "Diffview: open (working tree)" },
      { "<leader>gc", "<cmd>DiffviewClose<cr>", desc = "Diffview: close" },
      { "<leader>gh", "<cmd>DiffviewFileHistory %<cr>", desc = "Diffview: current file history" },
      { "<leader>gH", "<cmd>DiffviewFileHistory<cr>", desc = "Diffview: branch/repo history" },
      { "<leader>gm", "<cmd>DiffviewOpen origin/HEAD...HEAD<cr>", desc = "Diffview: changes vs main" },
    },
  },

  -----------------------------------------------------------------------------
  -- neogit: a magit-like interactive git UI (stage, commit, branch, push, ...)
  -----------------------------------------------------------------------------
  {
    "NeogitOrg/neogit",
    dependencies = {
      "nvim-lua/plenary.nvim",
      "sindrets/diffview.nvim",
      "nvim-telescope/telescope.nvim",
    },
    cmd = "Neogit",
    config = function() require("neogit").setup({}) end,
    keys = {
      { "<leader>gg", "<cmd>Neogit<cr>", desc = "Neogit: open git UI" },
    },
  },

  -----------------------------------------------------------------------------
  -- fugitive: classic raw git command interface (:Git ...)
  -----------------------------------------------------------------------------
  {
    "tpope/vim-fugitive",
    cmd = { "Git", "G" },
    keys = {
      { "<leader>gs", vim.cmd.Git, desc = "Git status (fugitive)" },
    },
  },
}
