
local function preload()
    redis.replicate_commands()
    local time = redis.call('TIME')
    math.randomseed(tonumber(time[2]))

    for i=0, 100 do
        redis.call('SET', "profile_cache:" .. i, i)
    end
end

local function sum_keys()

    local sum = 0
    local matches = redis.call('KEYS', 'profile_cache:*')

    for _, key in ipairs(matches) do
        local val = redis.call('GET', key)
        sum = sum + tonumber(val)
    end

    return sum
end
