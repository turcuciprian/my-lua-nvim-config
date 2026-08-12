-- Load order matters: set leader + core remaps before lazy bootstraps plugins.
require("chip.set")
require("chip.remap")
require("chip.lazy")
