**Example 1: 查询模型别名列表**



Input: 

```
tccli clb DescribeModelAliases --cli-unfold-argument  \
    --Limit 20 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "ModelAliasSet": [
            {
                "Coefficient": {
                    "InputCoefficient": 25,
                    "InputCachedCoefficient": 3,
                    "OutputCoefficient": 100
                },
                "ModelAliasName": "gpt-4o",
                "Source": "BYOK",
                "Status": "Active",
                "ServiceProviderCoefficientSet": [
                    {
                        "ServiceProviderId": "byok-52mdfb352",
                        "ServiceProviderName": "openai-direct",
                        "Coefficient": {
                            "InputCoefficient": 40,
                            "InputCachedCoefficient": 5,
                            "OutputCoefficient": 160
                        }
                    },
                    {
                        "ServiceProviderId": "byok-7a1c9e02",
                        "ServiceProviderName": "openai-proxy"
                    }
                ]
            }
        ],
        "TotalCount": 7,
        "RequestId": "1f58bf6f-3576-4f1a-9f33-8ffdf9917369"
    }
}
```

