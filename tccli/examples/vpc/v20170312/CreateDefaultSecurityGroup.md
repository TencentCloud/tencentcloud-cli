**Example 1: 创建默认安全组**



Input: 

```
tccli vpc CreateDefaultSecurityGroup --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SecurityGroup": {
            "SecurityGroupId": "sg-r0g2kty7",
            "SecurityGroupName": "default",
            "SecurityGroupDesc": "System created security group",
            "ProjectId": 0,
            "CreatedTime": "2020-01-10 11:37:52"
        },
        "RequestId": "727a8ab6-e15e-45db-8b8a-a95cb636a812"
    }
}
```

