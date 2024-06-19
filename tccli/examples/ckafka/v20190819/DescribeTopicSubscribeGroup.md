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
            "Status": 1,
            "TotalCount": 2,
            "StatusCountInfo": "1 Empty, 1 Stable",
            "GroupsInfo": [
                {
                    "Protocol": "",
                    "ProtocolType": "",
                    "ErrorCode": "0",
                    "State": "Empty",
                    "Members": [],
                    "Group": "xx1"
                },
                {
                    "Protocol": "roundrobin",
                    "ProtocolType": "consumer",
                    "ErrorCode": "0",
                    "State": "Stable",
                    "Members": [
                        {
                            "ClientHost": "10.0.0.0",
                            "MemberId": "consumer-63-/10.0.0.0-2022-07-31 19:09:08:169-73e4xx82-4c42-4ccf-8d01-7c74c8xxxxx2",
                            "ClientId": "consumer-63",
                            "Assignment": {
                                "Topics": [
                                    {
                                        "Topic": "xx_topic",
                                        "Partitions": [
                                            10
                                        ]
                                    }
                                ],
                                "Version": 0
                            }
                        }
                    ],
                    "Group": "xx2"
                }
            ]
        },
        "RequestId": "91b6b112-7f0a-4e18-b353-5202bcafd2c2"
    }
}
```

