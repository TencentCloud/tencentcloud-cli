**Example 1: 查询用户安全组配额**



Input: 

```
tccli ecm DescribeSecurityGroupLimits --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SecurityGroupLimitSet": {
            "SecurityGroupLimit": 50,
            "SecurityGroupPolicyLimit": 100,
            "SecurityGroupInstanceLimit": 2000,
            "InstanceSecurityGroupLimit": 2000,
            "ReferedSecurityGroupLimit": 10,
            "SecurityGroupModuleLimit": 10,
            "ModuleSecurityGroupLimit": 10
        },
        "RequestId": "6aa316a4-07d2-4355-b87d-40b7f22972b0"
    }
}
```

