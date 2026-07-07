**Example 1: 查询用户名下所有模型**

查询用户名下所有模型

Input: 

```
tccli clb DescribeModelNames --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ModelNames": [
            {
                "InputModalitiesUnion": [
                    "text"
                ],
                "ModelName": "gpt-4.1-pdf",
                "ServiceProviders": [
                    {
                        "InputModalities": [
                            "text"
                        ],
                        "ModelProvider": "openai",
                        "ServiceProviderId": "byok-qhygv05l",
                        "ServiceProviderName": "byok_test"
                    }
                ]
            }
        ],
        "TotalCount": 4,
        "RequestId": "7e0a2db8-1189-4282-8c76-35e2e75eee1e"
    }
}
```

