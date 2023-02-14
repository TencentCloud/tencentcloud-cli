**Example 1: 查询安全组被引用信息**

查询安全组被引用信息

Input: 

```
tccli vpc DescribeSecurityGroupReferences --cli-unfold-argument  \
    --SecurityGroupIds sg-12345678
```

Output: 
```
{
    "Response": {
        "ReferredSecurityGroupSet": [
            {
                "SecurityGroupId": "sg-12345678",
                "ReferredSecurityGroupIds": [
                    "sg-23456789",
                    "sg-13572468"
                ]
            }
        ],
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

