**Example 1: 发送cmq主题消息**



Input: 

```
tccli tdmq PublishCmqMsg --cli-unfold-argument  \
    --TopicName test-queue \
    --MsgContent testForPublish
```

Output: 
```
{
    "Response": {
        "Result": true,
        "MsgId": "1EAD5E05003A6767C1FC9160304F98",
        "RequestId": "3593f784-fcfb-4f23-b3dd-4751cba3aec7"
    }
}
```

