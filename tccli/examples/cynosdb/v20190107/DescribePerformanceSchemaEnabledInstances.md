**Example 1: 查询实例PFS设置**



Input: 

```
tccli cynosdb DescribePerformanceSchemaEnabledInstances --cli-unfold-argument  \
    --InstanceIds cynosdbmysql-ins-qjtwvlxa
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CollectStatus": "disable",
                "Consumers": [
                    "events_statements_history"
                ],
                "InstType": "master",
                "InstanceId": "cynosdbmysql-ins-qjtwvlxa",
                "Instruments": [
                    "wait/%"
                ]
            }
        ],
        "RequestId": "c54a5f28-b81d-4ebb-9e4b-d7cae879f119"
    }
}
```

