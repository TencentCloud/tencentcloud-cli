**Example 1: 创建消息转发配置**



Input: 

```
tccli iotvideoindustry CreateMessageForward --cli-unfold-argument  \
    --RegionId gz \
    --RegionName 广州 \
    --Instance ckafka \
    --InstanceName 卡夫卡 \
    --MessageType [1] \
    --TopicId topicid \
    --TopicName topicname
```

Output: 
```
{
    "Response": {
        "IntId": 1,
        "RequestId": "1d7a62c9-db36-4a5f-9209-2e420883e28f"
    }
}
```

