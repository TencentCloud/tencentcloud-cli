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
        "InstanceEnumParam": [
            {
                "CurrentValue": "yes",
                "DefaultValue": "yes",
                "EnumValue": [
                    "yes",
                    "no"
                ],
                "NeedRestart": "false",
                "ParamName": "auto-failback",
                "Status": 2,
                "Tips": "After the failure recovery, the master node is automatically switched back to the master zone (Standard) or the master node group (cluster)",
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
                "Unit": "ms",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "100",
                "DefaultValue": "100",
                "Max": "10000",
                "Min": "10",
                "NeedRestart": "false",
                "ParamName": "proxy-slowlog-log-slower-than",
                "Status": 2,
                "Tips": "the command will be record over this time in proxy",
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
                "CurrentValue": "\"\"",
                "DefaultValue": "\"\"",
                "EnumValue": [
                    "flushall",
                    "flushdb",
                    "keys",
                    "hgetall",
                    "eval",
                    "evalsha",
                    "script"
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
        "RequestId": "5585ef91-0749-478a-aa81-ecc7ee584143",
        "TotalCount": 7
    }
}
```

