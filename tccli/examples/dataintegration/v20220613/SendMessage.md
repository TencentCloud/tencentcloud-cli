**Example 1: 数据上报**



Input: 

```
tccli dataintegration SendMessage --cli-unfold-argument  \
    --Message.0.Body xx \
    --Message.0.Key xx \
    --Message.1.Body xx \
    --Message.1.Key xx \
    --DataHubId xx
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

