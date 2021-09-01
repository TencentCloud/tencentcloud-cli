**Example 1: 查询订阅某主题消息分组信息**



Input: 

```
tccli ckafka DescribeTopicSubscribeGroup --cli-unfold-argument  \
    --InstanceId ckafka-kmex0nvv \
    --TopicName test
```

Output: 
```
{
    "Response": {
        "Result": {
            "Status": 0,
            "TotalCount": 1,
            "StatusCountInfo": "xx",
            "GroupsInfo": [
                {
                    "Protocol": "xx",
                    "ProtocolType": "xx",
                    "ErrorCode": "xx",
                    "State": "xx",
                    "Members": [
                        {
                            "ClientHost": "xx",
                            "MemberId": "xx",
                            "ClientId": "xx",
                            "Assignment": {
                                "Topics": [
                                    {
                                        "Topic": "xx",
                                        "Partitions": [
                                            0
                                        ]
                                    }
                                ],
                                "Version": 0
                            }
                        }
                    ],
                    "Group": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

