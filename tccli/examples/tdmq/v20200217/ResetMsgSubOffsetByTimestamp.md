**Example 1: 回溯消息**



Input: 

```
tccli tdmq ResetMsgSubOffsetByTimestamp --cli-unfold-argument  \
    --EnvironmentId devNs \
    --TopicName devTopic \
    --Subscription devSub \
    --ToTimestamp 1730690396152 \
    --ClusterId pulsar-pnvjp9mbd947
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

