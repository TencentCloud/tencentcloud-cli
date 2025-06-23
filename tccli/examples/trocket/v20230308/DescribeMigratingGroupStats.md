**Example 1: 查看迁移消费组的实时信息**



Input: 

```
tccli trocket DescribeMigratingGroupStats --cli-unfold-argument  \
    --TaskId 02f6c31a-9707-4244-8dd3-35ad868ef92a \
    --GroupName group-a \
    --Namespace 
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "SourceConsumeLag": 0,
        "TargetConsumeLag": 0,
        "SourceConsumerClients": [
            {
                "ClientId": "client-a",
                "ClientAddr": "1.1.1.1",
                "Language": "JAVA",
                "Version": "5",
                "ConsumerLag": 0,
                "ChannelProtocol": ""
            }
        ],
        "TargetConsumerClients": [
            {
                "ClientId": "client-b",
                "ClientAddr": "2.2.2.2",
                "Language": "JAVA",
                "Version": "5.0",
                "ConsumerLag": 0
            }
        ],
        "RequestId": "02f6c31a-9707-4244-8dd3-35ad868ef92a"
    }
}
```

