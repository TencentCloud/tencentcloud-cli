**Example 1: 查看安全组**



Input: 

```
tccli ecm DescribeSecurityGroups --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Name security-group-id \
    --Filters.0.Values esg-05bb4upy \
    --Filters.1.Name security-group-name \
    --Filters.1.Values TestGroup
```

Output: 
```
{
    "Response": {
        "SecurityGroupSet": [
            {
                "SecurityGroupId": "esg-05bb4upy",
                "SecurityGroupName": "TestGroup",
                "SecurityGroupDesc": "test-group-desc",
                "IsDefault": "true",
                "TagSet": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

