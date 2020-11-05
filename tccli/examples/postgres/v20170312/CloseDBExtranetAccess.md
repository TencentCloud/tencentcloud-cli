**Example 1: Disabling public network link to instance**



Input: 

```
tccli postgres CloseDBExtranetAccess --cli-unfold-argument  \
    --DBInstanceId postgres-apzvwncr
```

Output: 
```
{
    "Response": {
        "FlowId": 1234,
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

