**Example 1: 发送一个消息**



Input: 

```
tccli tdmq SendMsg --cli-unfold-argument  \
    --EnvironmentId default \
    --TopicName cloud_test \
    --MsgContent one_msg
```

Output: 
```
{
    "Response": {
        "RequestId": "3593f784-fcfb-4f23-b3dd-4751cba3aec7"
    }
}
```

