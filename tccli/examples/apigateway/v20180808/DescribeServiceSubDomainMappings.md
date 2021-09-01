**Example 1: 查询自定义域名的路径映射**



Input: 

```
tccli apigateway DescribeServiceSubDomainMappings --cli-unfold-argument  \
    --ServiceId service-19c5fnhy \
    --SubDomain xxxxxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "IsDefaultMapping": false,
            "PathMappingSet": [
                {
                    "Path": "/",
                    "Environment": "release"
                }
            ]
        },
        "RequestId": "01c56ec2-6a40-46bc-bdf6-8b273d4bec93"
    }
}
```

