**Example 1: 测试示例**



Input: 

```
tccli tchousex DescribeEventList --cli-unfold-argument  \
    --InstanceId instance-yxin6btv \
    --StartEventId 0 \
    --Limit 10 \
    --ExtParameters.0.Name UserName \
    --ExtParameters.0.Value root \
    --ExtParameters.1.Name Password \
    --ExtParameters.1.Value Cdw12345
```

Output: 
```
{
    "Response": {
        "Events": [
            {
                "CatName": "hive",
                "DbName": "test",
                "EventId": 4,
                "EventTime": 1739434546,
                "EventType": "CREATE_TABLE",
                "Function": "",
                "Partitions": null,
                "TblName": "t1"
            },
            {
                "CatName": "hive",
                "DbName": "test",
                "EventId": 5,
                "EventTime": 1739434546,
                "EventType": "ALTER_TABLE",
                "Function": "",
                "Partitions": null,
                "TblName": "t1"
            }
        ],
        "HasMore": false,
        "NextEventId": 5,
        "RequestId": "116f2058-81c7-4733-b863-42a97683a3c7"
    }
}
```

