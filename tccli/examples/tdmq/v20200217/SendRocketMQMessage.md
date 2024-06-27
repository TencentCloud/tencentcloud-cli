**Example 1: 示例**



Input: 

```
tccli tdmq SendRocketMQMessage --cli-unfold-argument  \
    --ClusterId abc \
    --NamespaceId abc \
    --TopicName abc \
    --MsgKey abc \
    --MsgTag abc \
    --MsgBody abc
```

Output: 
```
{
    "Response": {
        "Result": true,
        "MsgId": "abc",
        "RequestId": "abc"
    }
}
```

