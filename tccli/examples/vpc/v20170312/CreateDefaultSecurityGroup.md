**Example 1: 创建默认安全组**



Input: 

```
tccli vpc CreateDefaultSecurityGroup --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SecurityGroup": {
            "SecurityGroupId": "sg-12345678",
            "SecurityGroupName": "test",
            "SecurityGroupDesc": "test",
            "ProjectId": "0",
            "CreateTime": "2018-01-13 19:26:33"
        }
    }
}
```

