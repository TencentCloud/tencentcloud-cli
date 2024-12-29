**Example 1: 删除治理中心命名空间**



Input: 

```
tccli tse DeleteGovernanceNamespaces --cli-unfold-argument  \
    --InstanceId ins-id \
    --GovernanceNamespaces.0.Name name
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

