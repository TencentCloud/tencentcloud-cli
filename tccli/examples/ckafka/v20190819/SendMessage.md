**Example 1: DataHubHTTP 发送消息**

HTTP协议接入点

Input: 

```
tccli ckafka SendMessage --cli-unfold-argument  \
    --DataHubId datahub-meuh9nhn \
    --Message.0.Key  \
    --Message.0.Body vvvvsdgsgshhh \
    --Message.1.Key  \
    --Message.1.Body vvvhhhhhhvsdgsgshhh
```

Output: 
```
{
    "Response": {
        "RequestId": "20e995ed-75b9-43bb-84c0-35676567e1a8",
        "MessageId": [
            "646174616875622d6d657568396e686e3a6465736372696265436c6f75644170693a343a3236313838",
            "875622d6d657568396e686e3a6465736372696265436c6f75644170693a343a3236323337"
        ]
    }
}
```

