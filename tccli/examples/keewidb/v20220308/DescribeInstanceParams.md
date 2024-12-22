**Example 1: 示例1**



Input: 

```
tccli keewidb DescribeInstanceParams --cli-unfold-argument  \
    --InstanceId kee-9clk****
```

Output: 
```
{
    "Response": {
        "InstanceEnumParam": [],
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
                "CurrentValue": "100",
                "DefaultValue": "100",
                "Max": "10000",
                "Min": "10",
                "NeedRestart": "false",
                "ParamName": "slowlog-log-slower-than",
                "Status": 2,
                "Tips": "Over this time the command is recorded in us.a negative number disables the slow log,a value of zero forces the logging of every command",
                "Unit": "ms",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "128",
                "DefaultValue": "128",
                "Max": "1024",
                "Min": "0",
                "NeedRestart": "false",
                "ParamName": "slowlog-max-len",
                "Status": 2,
                "Tips": "When a new command is logged and the slow log is already at its maximum length, the oldest one is removed from the queue of logged commands in order to make space",
                "Unit": "",
                "ValueType": "integer"
            }
        ],
        "InstanceMultiParam": [
            {
                "CurrentValue": "hgetall,eval",
                "DefaultValue": "hgetall",
                "EnumValue": [
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
                    "rpoplpush",
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
        "InstanceTextParam": [],
        "RequestId": "a4abf600-2813-4c5b-a3f8-fc4268efd151",
        "TotalCount": 5
    }
}
```

