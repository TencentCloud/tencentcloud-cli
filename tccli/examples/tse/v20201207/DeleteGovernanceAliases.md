**Example 1: 删除治理中心服务别名**



Input: 

```
tccli tse DeleteGovernanceAliases --cli-unfold-argument  \
    --InstanceId abc \
    --GovernanceAliases.0.Alias abc \
    --GovernanceAliases.0.AliasNamespace abc \
    --GovernanceAliases.0.Service abc \
    --GovernanceAliases.0.Namespace abc
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc"
    }
}
```

