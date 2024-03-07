**Example 1: 示例**

demo

Input: 

```
tccli tdmq DescribeRocketMQMsg --cli-unfold-argument  \
    --EnvironmentId e1 \
    --ClusterId c1 \
    --TopicName t1 \
    --PulsarMsgId p1 \
    --MsgId m1 \
    --QueryDlqMsg False
```

Output: 
```
{
    "Response": {
        "Body": "b",
        "MsgId": "m",
        "ProduceTime": "p",
        "RequestId": "r",
        "Properties": "p",
        "ProducerAddr": "p",
        "ShowTopicName": "s",
        "MessageTracks": []
    }
}
```

