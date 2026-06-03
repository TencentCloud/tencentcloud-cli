**Example 1: 查询是否绑定角色**



Input: 

```
tccli csip DescribeAssumeRole --cli-unfold-argument  \
    --RoleName TencentCloudRoleName
```

Output: 
```
{
    "Response": {
        "Bind": 1,
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

