**Example 1: 创建安全组**

创建安全组

Input: 

```
tccli vpc CreateSecurityGroup --cli-unfold-argument  \
    --GroupName TestGroup \
    --GroupDescription test-group-desc \
    --Tags.0.Value shanghai \
    --Tags.0.Key city
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SecurityGroup": {
            "SecurityGroupId": "sg-12345678",
            "SecurityGroupName": "TestGroup",
            "SecurityGroupDesc": "test-group-desc",
            "ProjectId": "0",
            "CreatedTime": "2018-01-13 19:26:33",
            "UpdateTime": "2018-01-13 19:26:33",
            "TagSet": [],
            "IsDefault": false
        }
    }
}
```

