**Example 1: 查询参数模板配额列表**



Input: 

```
tccli vpc DescribeTemplateLimits --cli-unfold-argument  \
    --Version 2017-03-12
```

Output: 
```
{
    "Response": {
        "TemplateLimit": {
            "AddressTemplateMemberLimit": 20,
            "AddressTemplateGroupMemberLimit": 20,
            "ServiceTemplateMemberLimit": 20,
            "ServiceTemplateGroupMemberLimit": 20
        },
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

