**Example 1: 查看迁移消费组的实时信息**



Input: 

```
tccli trocket DescribeMigratingGroupStats --cli-unfold-argument  \
    --TaskId taskId \
    --GroupName group-a \
    --Namespace 
```

Output: 
```
{
    "Response": {
        "SourceConsumeLag": 0,
        "TargetConsumeLag": 0,
        "SourceConsumerClients": [
            {
                "ClientId": "abc",
                "ClientAddr": "1.1.1.1",
                "Language": "JAVA",
                "Version": "5",
                "ConsumerLag": 0
            }
        ],
        "TargetConsumerClients": [
            {
                "ClientId": "abc",
                "ClientAddr": "2.2.2.2",
                "Language": "JAVA",
                "Version": "5.0",
                "ConsumerLag": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

