**Example 1: 删除治理中心服务别名**



Input: 

```
tccli tse DeleteGovernanceAliases --cli-unfold-argument  \
    --InstanceId ins-id \
    --GovernanceAliases.0.Alias alias \
    --GovernanceAliases.0.AliasNamespace alias-namespace \
    --GovernanceAliases.0.Service service \
    --GovernanceAliases.0.Namespace namespace
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

