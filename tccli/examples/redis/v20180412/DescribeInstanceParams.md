**Example 1: 查询实例参数列表**

查询指定实例的参数信息

Input: 

```
tccli redis DescribeInstanceParams --cli-unfold-argument  \
    --InstanceId crs-5a4p****
```

Output: 
```
{
    "Response": {
        "InstanceEnumParam": [
            {
                "CurrentValue": "yes",
                "DefaultValue": "yes",
                "EnumValue": [
                    "yes",
                    "no"
                ],
                "NeedRestart": "false",
                "ParamName": "lazyfree-lazy-eviction",
                "Status": 2,
                "Tips": "lazyfree switch on eviction",
                "ValueType": "enum"
            },
            {
                "CurrentValue": "yes",
                "DefaultValue": "yes",
                "EnumValue": [
                    "yes",
                    "no"
                ],
                "NeedRestart": "false",
                "ParamName": "lazyfree-lazy-expire",
                "Status": 2,
                "Tips": "lazyfree switch on expire",
                "ValueType": "enum"
            },
            {
                "CurrentValue": "yes",
                "DefaultValue": "yes",
                "EnumValue": [
                    "yes",
                    "no"
                ],
                "NeedRestart": "false",
                "ParamName": "lazyfree-lazy-server-del",
                "Status": 2,
                "Tips": "lazyfree switch on server implicit deletion",
                "ValueType": "enum"
            },
            {
                "CurrentValue": "noeviction",
                "DefaultValue": "noeviction",
                "EnumValue": [
                    "volatile-lru",
                    "volatile-lfu",
                    "allkeys-lru",
                    "allkeys-lfu",
                    "volatile-random",
                    "allkeys-random",
                    "volatile-ttl",
                    "noeviction"
                ],
                "NeedRestart": "false",
                "ParamName": "maxmemory-policy",
                "Status": 2,
                "Tips": "How Redis will select what to remove when maxmemory is reached",
                "ValueType": "enum"
            },
            {
                "CurrentValue": "yes",
                "DefaultValue": "yes",
                "EnumValue": [
                    "yes",
                    "no"
                ],
                "NeedRestart": "false",
                "ParamName": "replica-lazy-flush",
                "Status": 2,
                "Tips": "lazyfree switch on full resynchronization",
                "ValueType": "enum"
            },
            {
                "CurrentValue": "no",
                "DefaultValue": "no",
                "EnumValue": [
                    "yes",
                    "no"
                ],
                "NeedRestart": "false",
                "ParamName": "sentineauth",
                "Status": 2,
                "Tips": "Executing a sentinel order eliminates the password",
                "ValueType": "enum"
            }
        ],
        "InstanceIntegerParam": [
            {
                "CurrentValue": "15000",
                "DefaultValue": "15000",
                "Max": "120000",
                "Min": "15000",
                "NeedRestart": "false",
                "ParamName": "cluster-node-timeout",
                "Status": 2,
                "Tips": "Cluster node timeout is the amount of milliseconds a node must be unreachable for it to be considered in failure state",
                "Unit": "",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "512",
                "DefaultValue": "512",
                "Max": "10000",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "hash-max-ziplist-entries",
                "Status": 2,
                "Tips": "Hashes are encoded using a memory efficient data structure when they have a small number of entries",
                "Unit": "",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "64",
                "DefaultValue": "64",
                "Max": "10000",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "hash-max-ziplist-value",
                "Status": 2,
                "Tips": "Hashes are encoded using a memory efficient data structure when the biggest entry does not exceed a given threshold",
                "Unit": "",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "10",
                "DefaultValue": "10",
                "Max": "500",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "hz",
                "Status": 2,
                "Tips": "The frequency at which Redis background tasks are performed. A higher value results in higher CPU consumption but smaller latency. We recommend that you do not specify a value larger than 100.",
                "Unit": "",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "500",
                "DefaultValue": "500",
                "Max": "1000",
                "Min": "10",
                "NeedRestart": "false",
                "ParamName": "proxy-slowlog-log-slower-than",
                "Status": 2,
                "Tips": "the commands over this time will in proxy",
                "Unit": "ms",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "512",
                "DefaultValue": "512",
                "Max": "10000",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "set-max-intset-entries",
                "Status": 2,
                "Tips": "When a set is composed of just strings that happen to be integers in radix 10 in the range of 64 bit signed integers.",
                "Unit": "",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "10",
                "DefaultValue": "10",
                "Max": "1000",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "slowlog-log-slower-than",
                "Status": 2,
                "Tips": "Over this time the command is recorded in us.a negative number disables the slow log,a value of zero forces the logging of every command",
                "Unit": "ms",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "31536000",
                "DefaultValue": "31536000",
                "Max": "2147483647",
                "Min": "60",
                "NeedRestart": "false",
                "ParamName": "timeout",
                "Status": 2,
                "Tips": "Close the connection after a client is idle for N seconds",
                "Unit": "",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "128",
                "DefaultValue": "128",
                "Max": "10000",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "zset-max-ziplist-entries",
                "Status": 2,
                "Tips": "Sorted sets are encoded using a memory efficient data structure when they have a small number of entries.",
                "Unit": "",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "64",
                "DefaultValue": "64",
                "Max": "10000",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "zset-max-ziplist-value",
                "Status": 2,
                "Tips": "Sorted sets are encoded using a memory efficient data structure when the biggest entry does not exceed a given threshold.",
                "Unit": "",
                "ValueType": "integer"
            }
        ],
        "InstanceMultiParam": [
            {
                "CurrentValue": "\"\"",
                "DefaultValue": "\"\"",
                "EnumValue": [
                    "flushall",
                    "flushdb",
                    "keys",
                    "hgetall",
                    "eval",
                    "evalsha",
                    "script",
                    "scan",
                    "psetex",
                    "set",
                    "hmset",
                    "hset",
                    "lpush",
                    "rpush",
                    "sadd",
                    "zadd",
                    "del",
                    "mget",
                    "mset",
                    "bitop",
                    "exists",
                    "msetnx",
                    "blpop",
                    "brpop",
                    "rpoplpush",
                    "brpoplpush",
                    "smove",
                    "sunion",
                    "sinter",
                    "sdiff",
                    "sunionstore",
                    "sinterstore",
                    "sdiffstore",
                    "zunionstore",
                    "zinterstore",
                    "pfmerge",
                    "pfcount"
                ],
                "NeedRestart": "false",
                "ParamName": "disable-command-list",
                "Status": 2,
                "Tips": "commands in such config will not be allowed to run in this instance,you can config multi commands like this 'flushdb,keys'",
                "ValueType": "multi"
            }
        ],
        "InstanceTextParam": [
            {
                "CurrentValue": "\"\"",
                "DefaultValue": "\"\"",
                "NeedRestart": "false",
                "ParamName": "notify-keyspace-events",
                "Status": 2,
                "TextValue": [
                    "K",
                    "E",
                    "g",
                    "$",
                    "l",
                    "s",
                    "h",
                    "z",
                    "x",
                    "e",
                    "A"
                ],
                "Tips": "Changes in key space notification to registered clients",
                "ValueType": "text"
            }
        ],
        "RequestId": "a4abf600-2813-4c5b-a3f8-fc4268efd151",
        "TotalCount": 18
    }
}
```

