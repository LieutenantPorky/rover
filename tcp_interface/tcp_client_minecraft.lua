--VARIABLES
local event = require("event")
local net = require("internet")
local term = require("term")
local os = require("os")

local running = true
local ip = "localhost"
local port = 9999
local con = net.open(ip, port)
if con then
    print('Connected to the server! IP: ' .. ip .. ' port: ' .. port)
    con:close()
else
    print('connection failed')
    return 0
end

--FUNCTIONS
function sendString(s)
    if s == 'exit\n' then
      os.exit()
    end
    local con = net.open(ip, port)
    con:write(s)
    print('Sending ' .. string.sub(s,1,s:len()-1) .. ' to server...')
    con:flush()
    con:close()
end

while running do
    local s = term.read()
    sendString(s)
    os.sleep(0)
end
