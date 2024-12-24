**Example 1: 修改治理中心服务别名**



Input: 

```
tccli tse ModifyGovernanceAlias --cli-unfold-argument  \
    --InstanceId ins-id \
    --Alias alias \
    --AliasNamespace alias-namespace \
    --Service service \
    --Namespace namespace \
    --Comment comment
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

