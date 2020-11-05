**Example 1: Querying the path mappings of custom domain name**



Input: 

```
tccli apigateway DescribeServiceSubDomainMappings --cli-unfold-argument  \
    --ServiceId service-19c5fnhy\
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

