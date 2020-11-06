**Example 1: 查询发布订阅列表**



Input: 

```
tccli sqlserver DescribePublishSubscribe --cli-unfold-argument  \
    --InstanceId mssql-12klhrx2c \
    --PubOrSubInstanceId mssql-hh598yjo \
    --PubOrSubInstanceIp 10.0.1.27 \
    --PublishSubscribeId 5 \
    --PublishSubscribeName Change_name \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "PublishSubscribeSet": [
            {
                "Id": 5,
                "Name": "Change_name",
                "PublishInstanceId": "mssql-12klhrx2c",
                "PublishInstanceName": "890d5f71-7e4d-493c-bbe8-22fcec655d50",
                "PublishInstanceIp": "192.168.0.7",
                "SubscribeInstanceId": "mssql-hh598yjo",
                "SubscribeInstanceName": "1957199f-f396-47b6-9716-dfae74161f10",
                "SubscribeInstanceIp": "10.0.1.27",
                "DatabaseTupleSet": [
                    {
                        "PublishDatabase": "test01",
                        "SubscribeDatabase": "test01",
                        "LastSyncTime": "2020-07-13 16:57:01",
                        "Status": "SyncNormal"
                    },
                    {
                        "PublishDatabase": "test02",
                        "SubscribeDatabase": "test02",
                        "LastSyncTime": "2020-07-13 16:57:01",
                        "Status": "SyncNormal"
                    }
                ]
            }
        ],
        "RequestId": "b1475330-2c4d-49a7-b063-f3e8b69d23ca",
        "TotalCount": 1
    }
}
```

