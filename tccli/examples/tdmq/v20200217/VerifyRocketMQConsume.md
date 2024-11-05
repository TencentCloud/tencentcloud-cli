**Example 1: 消费验证示例**



Input: 

```
tccli tdmq VerifyRocketMQConsume --cli-unfold-argument  \
    --NamespaceId test_namespace \
    --MsgId 092BAE5A1656070DEA4E276DF0760089 \
    --ClusterId rocketmq-4k4orqgq \
    --GroupId test_group \
    --TopicName test_topic \
    --ClientId 9.43.174.90@18834#7187709773375173
```

Output: 
```
{
    "Response": {
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7"
    }
}
```

