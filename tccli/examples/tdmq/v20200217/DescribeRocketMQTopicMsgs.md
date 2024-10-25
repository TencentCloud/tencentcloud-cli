**Example 1: 获取消息列表**



Input: 

```
tccli tdmq DescribeRocketMQTopicMsgs --cli-unfold-argument  \
    --ClusterId rocketmq-zpz97455xwap \
    --EnvironmentId test_namespace \
    --TopicName test_topic \
    --MsgId 092BAE5A1656070DEA4E276DF0760089 \
    --MsgKey test_key \
    --StartTime 2023-10-08 15:44:59 \
    --EndTime 2023-10-08 16:14:59 \
    --Offset 0 \
    --Limit 20 \
    --TaskRequestId 2e5ecbb3-f2d6-49d3-9c82-8648f8ed8748 \
    --QueryDlqMsg True \
    --NumOfLatestMsg 0 \
    --Tag test_tag \
    --QueryDeadLetterMessage True
```

Output: 
```
{
    "Response": {
        "RequestId": "e3bba45e-876a-4107-ad5d-88006c1ddba2",
        "TotalCount": 1,
        "TopicMsgLogSets": [
            {
                "MsgId": "092BAE5A1656070DEA4E276DF0760089",
                "MsgTag": "test_tag",
                "MsgKey": "test_key",
                "ProducerAddr": "9.43.174.90",
                "ProduceTime": "2023-10-08 15:45:16",
                "PulsarMsgId": "092BAE5A1656070DEA4E276DF0760089",
                "DeadLetterResendTimes": 10,
                "ResendSuccessCount": 10
            }
        ],
        "TaskRequestId": "df71cc0a-3057-416b-b878-f0fe015e9913"
    }
}
```

