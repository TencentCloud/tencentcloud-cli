**Example 1: 查询实例参数列表**



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
                "Tips": "当系统到达设定的最大内存值后选择内存交换的策略",
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
                "Tips": "集群模式下当节点在指定时间内(毫秒)不可达则被认为处于失败状态",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "511",
                "DefaultValue": "512",
                "Max": "10000",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "hash-max-ziplist-entries",
                "Tips": "当哈希元素数量没有超过指定数目，则编码为内存利用率更高的数据结构存储",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "61",
                "DefaultValue": "64",
                "Max": "10000",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "hash-max-ziplist-value",
                "Tips": "当哈希中最大项没有超过指定阈值，则编码为内存利用率更高的数据结构存储",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "511",
                "DefaultValue": "512",
                "Max": "10000",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "set-max-intset-entries",
                "Tips": "当集合中的元素全部是64位有符号十进制整数并且未超过设定阈值，则编码为整数集合存储",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "10001",
                "DefaultValue": "10000",
                "Max": "1000000",
                "Min": "-1",
                "NeedRestart": "false",
                "ParamName": "slowlog-log-slower-than",
                "Tips": "超过指定时间的命令将会被记录，负数表示关闭该功能，零值表示强制记录所有命令的执行记录",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "4",
                "DefaultValue": "0",
                "Max": "7200",
                "Min": "0",
                "NeedRestart": "false",
                "ParamName": "timeout",
                "Tips": "客户端空闲指定时长后关闭连接，零值表示关闭该功能",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "121",
                "DefaultValue": "128",
                "Max": "10000",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "zset-max-ziplist-entries",
                "Tips": "当有序集合元素数量没有超过指定数目，则编码为内存利用率更高的数据结构存储",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "61",
                "DefaultValue": "64",
                "Max": "10000",
                "Min": "1",
                "NeedRestart": "false",
                "ParamName": "zset-max-ziplist-value",
                "Tips": "当有序集合中最大项没有超过指定阈值，则编码为内存利用率更高的数据结构存储",
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
                "Tips": "改变系统已设定客户端的键空间通知方式",
                "ValueType": "text"
            }
        ],
        "RequestId": "e546784b-709c-401d-aba6-73037eb4e522",
        "TotalCount": 10
    }
}
```

