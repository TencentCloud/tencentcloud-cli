**Example 1: 成功发送多条消息**



Input: 

```
tccli tdmq SendBatchMessages --cli-unfold-argument  \
    --Topic tenant/namespace/topic \
    --Payload '"hello TDMQ"'
```

Output: 
```
{
    "Response": {
        "RequestId": "36713f94-d07d-4b96-babf-42d139276f23",
        "MessageId": "71:12:0:0",
        "ErrorMsg": ""
    }
}
```

