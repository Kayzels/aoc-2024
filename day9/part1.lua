---@class Position
---@field value integer
---@field count integer

---@param info string
---@return Position[]
local function to_position(info)
	local current_val = 0
	---@type Position[]
	local positions = {}
	for index = 1, info:len() do
		local char = info:sub(index, index)
		local num = tonumber(char)
		if num then
			if index % 2 == 0 then
				---@type Position
				local position = { value = -1, count = num }
				table.insert(positions, position)
			else
				---@type Position
				local position = { value = current_val, count = num }
				table.insert(positions, position)
				current_val = current_val + 1
			end
		end
	end
	return positions
end

---@param positions Position[]
---@param func fun(pos: Position) : boolean
---@return Position[]
local function filter(positions, func)
	local new_index = 1
	local size_orig = #positions
	for _, v in ipairs(positions) do
		if func(v) then
			positions[new_index] = v
			new_index = new_index + 1
		end
	end
	for i = new_index, size_orig do
		positions[i] = nil
	end
	return positions
end

---@param positions Position[]
---@return Position[]
local function convert(positions)
	local first_ind = 1
	local last_ind = #positions

	while first_ind < last_ind do
		local first_pos = positions[first_ind]
		while first_pos.value >= 0 do
			first_ind = first_ind + 1
			first_pos = positions[first_ind]
		end

		local last_pos = positions[last_ind]
		while last_pos.count <= 0 or last_pos.value < 0 do
			last_ind = last_ind - 1
			last_pos = positions[last_ind]
		end

		if first_ind >= last_ind then
			break
		end

		if first_pos.count <= last_pos.count then
			local new_val = { value = last_pos.value, count = first_pos.count }
			local update_last = { value = last_pos.value, count = last_pos.count - first_pos.count }
			positions[first_ind] = new_val
			positions[last_ind] = update_last
		else
			local new_val = { value = last_pos.value, count = last_pos.count }
			local update_last = { value = last_pos.value, count = last_pos.count - first_pos.count }
			positions[first_ind] = new_val
			positions[last_ind] = update_last
			table.insert(positions, first_ind + 1, { value = -1, count = first_pos.count - last_pos.count })
		end
	end

	positions = filter(positions, function(pos)
		return pos.value >= 0 and pos.count > 0
	end)

	return positions
end

---@param positions Position[]
---@return integer
local function calculate(positions)
	local index = 0
	local acc = 0
	for _, position in ipairs(positions) do
		if position.value < 0 then
			goto continue
		end
		for i = 0, position.count - 1 do
			acc = acc + position.value * (index + i)
		end
    index = index + position.count
		::continue::
	end
	return acc
end

---@param path string
---@return string?
local function read_file(path)
  local file = io.open(path, "r")
  if not file then return end
  local content = file:read("*a")
  file:close()
  return content
end

local info = read_file("./day9/test_input")
if info ~= nil then
  local positions = convert(to_position(info))
  print(calculate(positions))
end
