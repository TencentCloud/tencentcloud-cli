**Example 1: 查询模型（包含多模态能力）和Key信息**

查询模型（包含多模态能力）和Key信息

Input: 

```
tccli clb DescribeModelKeys --cli-unfold-argument  \
    --ServiceProviderIds byok-lfwolo91
```

Output: 
```
{
    "Response": {
        "Models": [
            {
                "AccessType": "PublicCustom",
                "ApiBase": "http://11.141.93.26:10000/v1",
                "CreatedAt": "2026-06-01T07:37:25+00:00",
                "HostHeader": null,
                "KeyCount": 3,
                "Keys": [
                    {
                        "CreatedAt": "2026-06-01T07:37:25+00:00",
                        "KeyId": "mkey-qd6kwrnt",
                        "Name": "sk-1"
                    }
                ],
                "ModelIdsWithAlias": [
                    {
                        "AssociatedModelRouters": [],
                        "InputModalities": [
                            "text"
                        ],
                        "ModelAlias": "my-gpt-4o",
                        "ModelId": "gpt-4o",
                        "ProbedInputModalities": [
                            "text"
                        ]
                    }
                ],
                "ModelProvider": "openai",
                "Protocol": "openai",
                "ServiceIps": [],
                "ServiceProviderId": "byok-lfwolo91",
                "ServiceProviderName": null,
                "Status": "Active",
                "SubnetId": null,
                "Tags": [
                    {
                        "TagKey": "text",
                        "TagValue": "text"
                    }
                ],
                "VerifySSL": true,
                "VpcId": null
            }
        ],
        "TotalCount": 1,
        "RequestId": "d4ac361b-35ee-47b0-95b1-a5051c483c57"
    }
}
```

