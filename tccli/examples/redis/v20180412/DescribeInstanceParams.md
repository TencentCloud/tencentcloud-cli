**Example 1: Querying the list of instance parameters**



Input: 

```
tccli redis DescribeInstanceParams --cli-unfold-argument  \
    --InstanceId crs-5a4py64p
```

Output: 
```
{
    "Response": {
        "InstanceEnumParam": [
            {
                "CurrentValue": "volatile-ttl",
                "DefaultValue": "noeviction",
                "EnumValue": [
                    "volatile-lru",
                    "allkeys-lru",
                    "volatile-random",
                    "allkeys-random",
                    "volatile-ttl",
                    "noeviction"
                ],
                "NeedRestart": "false",
                "ParamName": "maxmemory-policy",
                "Tips": "Select the memory swapping policy when the system reaches the set maximum memory value",
                "ValueType": "enum"
            }
        ],
        "InstanceIntegerParam": [
            {
                "CurrentValue": "15001",
                "DefaultValue": "15000",
                "Max": "120000",
                "Min": "15000",
                "NeedRestart": "false",
                "ParamName": "cluster-node-timeout",
                "Tips": "In cluster mode, a node is considered to fail if it is unreachable within the specified time period (in milliseconds)",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "511",
                "DefaultValue": "512",
                "Max": "10000",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "hash-max-ziplist-entries",
                "Tips": "If the number of hash entries does not exceed the specified number, the hashes are encoded using a memory efficient data structure",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "61",
                "DefaultValue": "64",
                "Max": "10000",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "hash-max-ziplist-value",
                "Tips": "If the largest item in the hashes does not exceed the specified threshold, the hashes are encoded using a memory efficient data structure",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "511",
                "DefaultValue": "512",
                "Max": "10000",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "set-max-intset-entries",
                "Tips": "If all the elements in the set are 64-bit signed decimal integers and do not exceed the set threshold, the hashes are encoded as an integer set",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "10001",
                "DefaultValue": "10000",
                "Max": "1000000",
                "Min": "-1",
                "NeedRestart": "false",
                "ParamName": "slowlog-log-slower-than",
                "Tips": "Commands that exceed the specified time period of execution will be logged; a negative number indicates to disable this feature, and zero indicates to compulsorily log the executions of all commands",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "4",
                "DefaultValue": "0",
                "Max": "7200",
                "Min": "0",
                "NeedRestart": "false",
                "ParamName": "timeout",
                "Tips": "The connection is closed after the client is idle for the specified length of time, and zero indicates to disable this feature",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "121",
                "DefaultValue": "128",
                "Max": "10000",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "zset-max-ziplist-entries",
                "Tips": "If the number of ordered set elements does not exceed the specified number, the hashes are encoded using a memory efficient data structure",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "61",
                "DefaultValue": "64",
                "Max": "10000",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "zset-max-ziplist-value",
                "Tips": "If the largest item in the ordered set does not exceed the specified threshold, the hashes are encoded using a memory efficient data structure",
                "ValueType": "integer"
            }
        ],
        "InstanceTextParam": [
            {
                "CurrentValue": "\"eK\"",
                "DefaultValue": "\"\"",
                "NeedRestart": "false",
                "ParamName": "notify-keyspace-events",
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
                "Tips": "Change the notification method of the client key space set by the system",
                "ValueType": "text"
            }
        ],
        "RequestId": "e546784b-709c-401d-aba6-73037eb4e522",
        "TotalCount": 10
    }
}
```

