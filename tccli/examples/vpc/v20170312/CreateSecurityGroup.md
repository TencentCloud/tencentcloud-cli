**Example 1: 创建安全组**



Input: 

```
tccli vpc CreateSecurityGroup --cli-unfold-argument  \
    --Version 2017-03-12 \
    --GroupName TestGroup \
    --GroupDescription test-group-desc \
    --Tags.0.Key city \
    --Tags.0.Value shanghai
```

Output: 
```
{
    "Response": {
        "SecurityGroup": {
            "SecurityGroupId": "sg-3g7ftkp3",
            "SecurityGroupName": "TestGroup",
            "SecurityGroupDesc": "test-group-desc",
            "ProjectId": "0",
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

