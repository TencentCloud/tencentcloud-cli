**Example 1: 证书查询关联资源**

证书查询关联资源

Input: 

```
tccli ssl DescribeDeployedResources --cli-unfold-argument  \
    --ResourceType xx \
    --CertificateIds xx
```

Output: 
```
{
    "Response": {
        "DeployedResources": [
            {
                "CertificateId": "xx",
                "ResourceIds": null,
                "Resources": [],
                "Type": "xx",
                "Count": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

