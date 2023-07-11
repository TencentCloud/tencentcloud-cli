**Example 1: 证书查询关联资源**

证书查询关联资源

Input: 

```
tccli ssl DescribeDeployedResources --cli-unfold-argument  \
    --ResourceType xx1 \
    --CertificateIds xx1
```

Output: 
```
{
    "Response": {
        "DeployedResources": [
            {
                "CertificateId": "xx1",
                "ResourceIds": null,
                "Resources": [],
                "Type": "xx1",
                "Count": 0
            }
        ],
        "RequestId": "xx1-xxx"
    }
}
```

