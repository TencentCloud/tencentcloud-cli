**Example 1: 获取消费分组信息**



Input: 

```
tccli ckafka DescribeGroupInfo --cli-unfold-argument  \
    --InstanceId ckafka-ivn43n20 \
    --GroupList groupName
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "ErrorCode": "0",
                "State": "Stable",
                "ProtocolType": "consumer",
                "Protocol": "range",
                "Members": [
                    {
                        "MemberId": "consumer-1-/10.53.88.65-2018-08-10 10:17:19:639-88206ef1-9248-43a0-9ff4-e22c3ab21e92",
                        "ClientId": "consumer-1",
                        "ClientHost": "/10.53.88.65",
                        "Assignment": {
                            "Version": 0,
                            "Topics": [
                                {
                                    "Topic": "test",
                                    "Partitions": [
                                        0
                                    ]
                                }
                            ]
                        }
                    }
                ],
                "Group": "perf-consumer-97910"
            }
        ],
        "RequestId": "8e9b234e-0c3e-4340-9733-adbd05879b10"
    }
}
```

