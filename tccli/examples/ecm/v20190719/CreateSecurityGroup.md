**Example 1: 创建安全组**



Input: 

```
tccli ecm CreateSecurityGroup --cli-unfold-argument  \
    --GroupName TestGroup\
    --GroupDescription test-group-desc\
    --Tags.0.Key city\
    --Tags.0.Value shanghai
```

Output: 
```
{
    "Response": {
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SecurityGroup": {
            "SecurityGroupId": "esg-3g7ftkp3",
            "SecurityGroupName": "TestGroup",
            "SecurityGroupDesc": "test-group-desc",
            "ProjectId": "0",
            "CreateTime": "2020-05-13 19:26:33",
            "TagSet": [
                {
                    "Key": "city",
                    "Value": "shanghai"
                }
            ]
        }
    }
}
```

