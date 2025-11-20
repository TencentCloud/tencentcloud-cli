**Example 1: DescribeMongoDbProcessList示例**

DescribeMongoDbProcessList示例

Input: 

```
tccli dbbrain DescribeMongoDBProcessList --cli-unfold-argument  \
    --InstanceId cmgo-3bfxr69z \
    --Product mongodb
```

Output: 
```
{
    "Response": {
        "ProcessList": {
            "Data": [
                {
                    "Command": "{\"shard\": \"cmgo-8hnz2qj1_1\",\"type\": \"op\",\"host\": \"TENCENT64.site:7037\",\"desc\": \"conn15849513\",\"connectionId\": {\"$numberInt\":\"158",
                    "DB": "follows_1600088807.$cmd",
                    "Host": "9.222.21.122:53642",
                    "ID": 1798318411,
                    "InstanceNodeId": "mongos-3",
                    "IsInternalIp": true,
                    "ShardName": "cmgo-8hnz2qj1_1",
                    "Time": 97677.001,
                    "Type": "command",
                    "User": "mongouser"
                }
            ],
            "Names": [
                "ID",
                "Host",
                "DB",
                "Command",
                "Time",
                "Type"
            ]
        },
        "RequestId": "96422ce1-7ffd-40c8-a8fd-304331bd7270"
    }
}
```

