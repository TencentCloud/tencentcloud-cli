**Example 1: 创建安全组**



Input: 

```
tccli ecm CreateSecurityGroup --cli-unfold-argument  \
    --GroupName demo \
    --GroupDescription demo \
    --Tags.0.Key city \
    --Tags.0.Value shanghai
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SecurityGroup": {
            "SecurityGroupId": "esg-3g7ftkp3",
            "SecurityGroupName": "demo",
            "SecurityGroupDesc": "demo",
            "CreatedTime": "2020-05-13 19:26:33",
            "IsDefault": false,
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

