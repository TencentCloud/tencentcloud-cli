**Example 1: 发送消息**



Input: 

```
tccli tdmq SendCmqMsg --cli-unfold-argument  \
    --QueueName test-queue \
    --MsgContent testforSend \
    --DelaySeconds 0
```

Output: 
```
{
    "Response": {
        "Result": true,
        "MsgId": "09A51113003621B8D17C0DF3DC2403DC",
        "RequestId": "3593f784-fcfb-4f23-b3dd-4751cba3aec7"
    }
}
```

