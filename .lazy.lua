return {
	"mfussenegger/nvim-dap",
	opts = function(_, opts)
		table.insert(require("dap").configurations.python, 1, {
			type = "python",
			request = "launch",
			name = "AOC Module",
			console = "integratedTerminal",
			module = "${relativeFileDirname}.${fileBasenameNoExtension}",
		})
	end,
}
