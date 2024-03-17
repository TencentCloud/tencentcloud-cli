**Example 1: 修改治理中心服务别名**



Input: 

```
tccli tse ModifyGovernanceAlias --cli-unfold-argument  \
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

