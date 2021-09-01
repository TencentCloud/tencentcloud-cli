**Example 1: 发送消息**



Input: 

```
tccli tdmq SendCmqMsg --cli-unfold-argument  \
    --QueueName test-queue \
    --MsgContent test \
    --DelaySeconds 0
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

