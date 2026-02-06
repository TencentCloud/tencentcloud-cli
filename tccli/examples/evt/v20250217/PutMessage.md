**Example 1: 推送消息**



Input: 

```
tccli evt PutMessage --cli-unfold-argument  \
    --EventId event-sdiq \
    --Data {"testkey":"testvalue"}
```

Output: 
```
{
    "Response": {
        "TicketId": "ticket-sydinq",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

