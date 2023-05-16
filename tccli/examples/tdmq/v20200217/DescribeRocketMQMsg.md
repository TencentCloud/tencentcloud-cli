**Example 1: 示例**

demo

Input: 

```
tccli tdmq DescribeRocketMQMsg --cli-unfold-argument  \
    --EnvironmentId xx \
    --ClusterId xx \
    --TopicName xx \
    --PulsarMsgId xx \
    --MsgId xx \
    --QueryDlqMsg False
```

Output: 
```
{
    "Response": {
        "Body": "xx",
        "MsgId": "xx",
        "ProduceTime": "xx",
        "RequestId": "xx",
        "Properties": "xx",
        "ProducerAddr": "xx",
        "ShowTopicName": "xx",
        "MessageTracks": []
    }
}
```

