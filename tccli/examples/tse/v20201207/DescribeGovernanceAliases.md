**Example 1: 查询治理中心服务别名**



Input: 

```
tccli tse DescribeGovernanceAliases --cli-unfold-argument  \
    --Service service \
    --Namespace namespace \
    --Alias alias \
    --AliasNamespace alias-namespace \
    --Comment comment \
    --Offset 1 \
    --Limit 1 \
    --InstanceId ins-id
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Content": [
            {
                "Alias": "alias",
                "AliasNamespace": "alias-namespace",
                "Service": "service",
                "Namespace": "namespace",
                "Comment": "comment",
                "CreateTime": "2024-10-08 10:00:00",
                "ModifyTime": "2024-10-08 10:00:00",
                "Id": "id",
                "Editable": true
            }
        ],
        "RequestId": "req-id"
    }
}
```

