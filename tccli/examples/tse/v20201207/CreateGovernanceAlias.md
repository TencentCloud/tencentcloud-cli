**Example 1: 创建治理中心服务别名**



Input: 

```
tccli tse CreateGovernanceAlias --cli-unfold-argument  \
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

