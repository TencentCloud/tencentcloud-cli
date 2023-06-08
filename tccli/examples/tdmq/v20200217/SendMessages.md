**Example 1: 成功发送单条消息**

成功发送单条消息
不支持非持久化topic

Input: 

```
tccli tdmq SendMessages --cli-unfold-argument  \
    --Topic tenant/namespace/topic \
    --Payload "hello TDMQ"
```

Output: 
```
{
    "Response": {
        "RequestId": "36713f94-d07d-4b96-babf-42d139276f23",
        "MessageId": "71:11:0:0",
        "ErrorMsg": ""
    }
}
```

