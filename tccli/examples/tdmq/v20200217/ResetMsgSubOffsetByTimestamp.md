**Example 1: 回溯消息**



Input: 

```
tccli tdmq ResetMsgSubOffsetByTimestamp --cli-unfold-argument  \
    --EnvironmentId default \
    --TopicName cloud_test \
    --Subscription cloud_sub \
    --ToTimestamp 1585901708600
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "3593f784-fcfb-4f23-b3dd-4751cba3aec7"
    }
}
```

