**Example 1: 创建治理中心服务别名**



Input: 

```
tccli tse CreateGovernanceAlias --cli-unfold-argument  \
    --InstanceId abc \
    --Alias abc \
    --AliasNamespace abc \
    --Service abc \
    --Namespace abc \
    --Comment abc
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

