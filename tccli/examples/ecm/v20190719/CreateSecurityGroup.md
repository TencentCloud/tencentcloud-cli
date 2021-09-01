**Example 1: 创建安全组**



Input: 

```
tccli ecm CreateSecurityGroup --cli-unfold-argument  \
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
            "SecurityGroupId": "esg-3g7ftkp3",
            "SecurityGroupName": "TestGroup",
            "SecurityGroupDesc": "test-group-desc",
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

