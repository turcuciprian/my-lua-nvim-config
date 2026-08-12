-- Telescope: fuzzy finder for files, project-wide grep, buffers, git, LSP, ...
return {
  "nvim-telescope/telescope.nvim",
  branch = "0.1.x",
  dependencies = {
    "nvim-lua/plenary.nvim",
    -- Native fzf sorter (compiled) for much faster matching
    { "nvim-telescope/telescope-fzf-native.nvim", build = "make" },
  },
  config = function()
    local telescope = require("telescope")
    telescope.setup({
      defaults = {
        path_display = { "truncate" },
        layout_strategy = "horizontal",
        layout_config = { prompt_position = "top" },
        sorting_strategy = "ascending",
      },
    })
    pcall(telescope.load_extension, "fzf")

    local builtin = require("telescope.builtin")
    local map = vim.keymap.set

    -- Files / project navigation
    map("n", "<leader>pf", builtin.find_files, { desc = "Find files (project)" })
    map("n", "<leader>ff", builtin.find_files, { desc = "Find files" })
    map("n", "<leader>pg", builtin.git_files, { desc = "Find git-tracked files" })
    map("n", "<C-p>", builtin.git_files, { desc = "Find git-tracked files" })
    map("n", "<leader>fo", builtin.oldfiles, { desc = "Recent files" })
    map("n", "<leader>fb", builtin.buffers, { desc = "Open buffers" })
    map("n", "<leader>fh", builtin.help_tags, { desc = "Help tags" })
    map("n", "<leader>fr", builtin.resume, { desc = "Resume last picker" })
    map("n", "<leader>fd", builtin.diagnostics, { desc = "Diagnostics (project)" })

    -- Project-wide search
    map("n", "<leader>fg", builtin.live_grep, { desc = "Live grep (project search)" })
    map("n", "<leader>fw", builtin.grep_string, { desc = "Grep word under cursor" })
    map("n", "<leader>ps", function()
      builtin.grep_string({ search = vim.fn.input("Grep > ") })
    end, { desc = "Grep for a prompt" })

    -- Git pickers (history / branches)
    map("n", "<leader>gl", builtin.git_commits, { desc = "Git commits (log)" })
    map("n", "<leader>gB", builtin.git_branches, { desc = "Git branches" })
  end,
}
