**Example 1: 发送cmq主题消息**



Input: 

```
tccli tdmq PublishCmqMsg --cli-unfold-argument  \
    --TopicName test-queue \
    --MsgContent test
```

Output: 
```
{
    "Response": {
        "Result": true,
        "MsgId": "50169152:0:0:-1",
        "RequestId": "3593f784-fcfb-4f23-b3dd-4751cba3aec7"
    }
}
```

