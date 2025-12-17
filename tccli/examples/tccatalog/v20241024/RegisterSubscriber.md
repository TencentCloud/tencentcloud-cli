**Example 1: RegisterSubscriber示例**



Input: 

```
tccli tccatalog RegisterSubscriber --cli-unfold-argument  \
    --SinkType pulsar \
    --SubscriberName wedata-113-xcvadfadsgad \
    --Description wedata subscriber \
    --Filters.0.Name AppId \
    --Filters.0.Values 133 113 1133 \
    --Filters.1.Name Operation \
    --Filters.1.Values CREATE_TABLE DROP_TABLE CREATE_SCHEMA DROP_SCHEMA CREATE_CATALOG DROP_CATALOG \
    --Params.0.Key url \
    --Params.0.Value pulsar://localhost:6650 \
    --Params.1.Key topic \
    --Params.1.Value wedata-113
```

Output: 
```
{
    "Response": {
        "RequestId": "helllllllo",
        "SubscriberId": "6864b571-1cbe-4bf1-8e6f-bbf78490366e"
    }
}
```

