**Example 1: 证书查询关联资源**

证书查询关联资源

Input: 

```
tccli ssl DescribeDeployedResources --cli-unfold-argument  \
    --ResourceType teo \
    --CertificateIds Tjs***jjs
```

Output: 
```
{
    "Response": {
        "DeployedResources": [
            {
                "CertificateId": "Tjs***jjs",
                "ResourceIds": [
                    "ins-******"
                ],
                "Resources": [
                    "inx-******"
                ],
                "Type": "teo",
                "Count": 1
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

