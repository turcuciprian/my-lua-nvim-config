-- LSP + autocompletion.
--   mason          -> installs language servers automatically
--   nvim-lspconfig -> server configs (enabled automatically by mason-lspconfig)
--   nvim-cmp       -> the completion engine (autocomplete)
--   LuaSnip        -> snippet expansion
return {
  -----------------------------------------------------------------------------
  -- Language servers
  -----------------------------------------------------------------------------
  {
    "neovim/nvim-lspconfig",
    dependencies = {
      { "williamboman/mason.nvim", config = true },
      "williamboman/mason-lspconfig.nvim",
      "hrsh7th/cmp-nvim-lsp",
    },
    config = function()
      require("mason").setup()
      require("mason-lspconfig").setup({
        ensure_installed = {
          "lua_ls",   -- Lua
          "pyright",  -- Python (type checking)
          "ruff",     -- Python (linting + formatting)
          "ts_ls",    -- TypeScript / JavaScript
          "bashls",   -- Bash
          "jsonls",   -- JSON
          "html",     -- HTML
          "cssls",    -- CSS
        },
      })

      -- Give every server the completion capabilities from nvim-cmp
      local capabilities = require("cmp_nvim_lsp").default_capabilities()
      vim.lsp.config("*", { capabilities = capabilities })

      -- Tell the Lua server that the global `vim` exists
      vim.lsp.config("lua_ls", {
        settings = {
          Lua = {
            diagnostics = { globals = { "vim" } },
            telemetry = { enable = false },
          },
        },
      })

      -- Buffer-local keymaps, set when a server attaches to a buffer
      vim.api.nvim_create_autocmd("LspAttach", {
        desc = "LSP actions",
        callback = function(event)
          local opts = { buffer = event.buf }
          local map = vim.keymap.set
          local builtin = require("telescope.builtin")

          map("n", "K", vim.lsp.buf.hover, opts)                     -- hover docs
          map("n", "gd", builtin.lsp_definitions, opts)              -- go to definition
          map("n", "gD", vim.lsp.buf.declaration, opts)              -- go to declaration
          map("n", "gi", builtin.lsp_implementations, opts)          -- go to implementation
          map("n", "go", builtin.lsp_type_definitions, opts)         -- go to type definition
          map("n", "gr", builtin.lsp_references, opts)               -- find references
          map("n", "gs", vim.lsp.buf.signature_help, opts)           -- signature help
          map("n", "<leader>rn", vim.lsp.buf.rename, opts)           -- rename symbol
          map("n", "<F2>", vim.lsp.buf.rename, opts)
          map("n", "<leader>ca", vim.lsp.buf.code_action, opts)      -- code action
          map("n", "<F4>", vim.lsp.buf.code_action, opts)
          map({ "n", "x" }, "<leader>cf", function()                 -- format
            vim.lsp.buf.format({ async = true })
          end, opts)
          map({ "n", "x" }, "<F3>", function()
            vim.lsp.buf.format({ async = true })
          end, opts)

          -- Diagnostics
          map("n", "<leader>cd", vim.diagnostic.open_float, opts)    -- line diagnostics
          map("n", "[d", function() vim.diagnostic.jump({ count = -1, float = true }) end, opts)
          map("n", "]d", function() vim.diagnostic.jump({ count = 1, float = true }) end, opts)
        end,
      })

      vim.diagnostic.config({ virtual_text = true, severity_sort = true })
    end,
  },

  -----------------------------------------------------------------------------
  -- Autocompletion engine
  -----------------------------------------------------------------------------
  {
    "hrsh7th/nvim-cmp",
    event = "InsertEnter",
    dependencies = {
      "hrsh7th/cmp-nvim-lsp",
      "hrsh7th/cmp-buffer",
      "hrsh7th/cmp-path",
      { "L3MON4D3/LuaSnip", dependencies = { "rafamadriz/friendly-snippets" } },
      "saadparwaiz1/cmp_luasnip",
    },
    config = function()
      local cmp = require("cmp")
      local luasnip = require("luasnip")
      require("luasnip.loaders.from_vscode").lazy_load()

      cmp.setup({
        snippet = {
          expand = function(args) luasnip.lsp_expand(args.body) end,
        },
        mapping = cmp.mapping.preset.insert({
          ["<C-Space>"] = cmp.mapping.complete(),       -- trigger completion
          ["<C-e>"] = cmp.mapping.abort(),              -- close menu
          ["<CR>"] = cmp.mapping.confirm({ select = true }), -- accept
          ["<C-n>"] = cmp.mapping.select_next_item(),
          ["<C-p>"] = cmp.mapping.select_prev_item(),
          ["<C-b>"] = cmp.mapping.scroll_docs(-4),
          ["<C-f>"] = cmp.mapping.scroll_docs(4),
          ["<Tab>"] = cmp.mapping(function(fallback)
            if cmp.visible() then cmp.select_next_item()
            elseif luasnip.expand_or_jumpable() then luasnip.expand_or_jump()
            else fallback() end
          end, { "i", "s" }),
          ["<S-Tab>"] = cmp.mapping(function(fallback)
            if cmp.visible() then cmp.select_prev_item()
            elseif luasnip.jumpable(-1) then luasnip.jump(-1)
            else fallback() end
          end, { "i", "s" }),
        }),
        sources = {
          { name = "nvim_lsp" },
          { name = "luasnip" },
          { name = "buffer" },
          { name = "path" },
        },
      })
    end,
  },
}
