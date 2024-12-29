**Example 1: 删除治理中心服务**



Input: 

```
tccli tse DeleteGovernanceServices --cli-unfold-argument  \
    --InstanceId ins-id \
    --GovernanceServices.0.Name name \
    --GovernanceServices.0.Namespace namespace
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "req-id"
    }
}
```

