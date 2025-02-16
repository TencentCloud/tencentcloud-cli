**Example 1: 证书查询关联资源**

证书查询关联资源

Input: 

```
tccli ssl DescribeDeployedResources --cli-unfold-argument  \
    --ResourceType clb \
    --CertificateIds EsF***1N
```

Output: 
```
{
    "Response": {
        "DeployedResources": [
            {
                "CertificateId": "EsF***1N",
                "ResourceIds": [
                    "lb-8kdm7***"
                ],
                "Resources": [
                    "lb-8kdm7***"
                ],
                "Type": "clb",
                "Count": 1
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

