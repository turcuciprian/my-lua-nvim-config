-- VS Code "Dark Modern" (the current default VS Code dark theme).
-- Syntax colors (Dark+ tokens, inherited by Dark Modern) are exact:
--   keywords #569CD6, control keywords #C586C0, comments #6A9955,
--   strings #CE9178, numbers #B5CEA8, types #4EC9B0, functions #DCDCAA,
--   variables #9CDCFE, escapes #D7BA7D, regexp #D16969
-- The overrides below pin the workbench colors to the exact values from
-- Microsoft's dark_modern.json (editor #1F1F1F/#CCCCCC, sidebar #181818, ...).
return {
  "Mofiqul/vscode.nvim",
  lazy = false,
  priority = 1000, -- load before everything else so highlights are correct
  config = function()
    require("vscode").setup({
      style = "dark",
      transparent = false, -- VS Code uses a solid #1F1F1F background
      italic_comments = false, -- Dark Modern does not italicize comments
      underline_links = true,
      -- File explorer gets the VS Code sidebar color (#181818, via vscLeftDark)
      disable_nvimtree_bg = false,

      color_overrides = {
        vscFront = "#CCCCCC", -- editor.foreground / foreground
        vscBack = "#1F1F1F", -- editor.background
        vscLineNumber = "#6E7681", -- editorLineNumber.foreground
        vscLeftDark = "#181818", -- sideBar.background
        vscLeftMid = "#181818", -- statusBar.background
        vscTabOther = "#181818", -- tab.inactiveBackground
        vscTabOutside = "#181818", -- editorGroupHeader.tabsBackground
        vscSearchCurrent = "#9E6A03", -- editor.findMatchBackground
        vscCursorDarkDark = "#282828", -- editor.lineHighlightBackground (rendered)
      },

      group_overrides = {
        -- editorLineNumber.activeForeground
        CursorLineNr = { fg = "#CCCCCC", bg = "#1F1F1F" },
        -- list.hoverBackground for the file explorer cursor line
        NvimTreeCursorLine = { bg = "#2A2D2E" },
        -- editorGutter.{added,modified,deleted}Background
        GitSignsAdd = { fg = "#2EA043" },
        GitSignsChange = { fg = "#0078D4" },
        GitSignsDelete = { fg = "#F85149" },
        -- editor{Error,Warning,Info,Hint}.foreground
        DiagnosticError = { fg = "#F14C4C" },
        DiagnosticWarn = { fg = "#CCA700" },
        DiagnosticInfo = { fg = "#3794FF" },
        DiagnosticHint = { fg = "#EEEEEE" },
        DiagnosticUnderlineError = { sp = "#F14C4C", undercurl = true },
        DiagnosticUnderlineWarn = { sp = "#CCA700", undercurl = true },
        DiagnosticUnderlineInfo = { sp = "#3794FF", undercurl = true },
        DiagnosticUnderlineHint = { sp = "#EEEEEE", undercurl = true },
      },
    })
    vim.cmd.colorscheme("vscode")
  end,
}
