**Example 1: 查询治理中心服务别名**



Input: 

```
tccli tse DescribeGovernanceAliases --cli-unfold-argument  \
    --Service abc \
    --Namespace abc \
    --Alias abc \
    --AliasNamespace abc \
    --Comment abc \
    --Offset 1 \
    --Limit 1 \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Content": [
            {
                "Alias": "abc",
                "AliasNamespace": "abc",
                "Service": "abc",
                "Namespace": "abc",
                "Comment": "abc",
                "CreateTime": "abc",
                "ModifyTime": "abc",
                "Id": "abc",
                "Editable": true
            }
        ],
        "RequestId": "abc"
    }
}
```

