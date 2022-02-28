**Example 1: CancelFlow**



Input: 

```
tccli ess CancelFlow --cli-unfold-argument  \
    --Operator.OpenId xx \
    --Operator.ClientIp xx \
    --Operator.UserId xx \
    --Operator.Channel xx \
    --Operator.ProxyIp xx \
    --FlowId xx \
    --CancelMessage xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx"
    }
}
```

