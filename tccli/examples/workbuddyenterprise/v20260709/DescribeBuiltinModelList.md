**Example 1: 查询内置模型列表**

分页查询内置模型列表，按启用状态过滤。

Input: 

```
tccli workbuddyenterprise DescribeBuiltinModelList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name Status \
    --Filters.0.Values ENABLED \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "BuiltinModelSet": [
            {
                "ModelId": "hunyuan-turbo",
                "Name": "混元 Turbo",
                "Vendor": "TENCENT",
                "MaxOutputTokens": 8192,
                "MaxInputTokens": 128000,
                "SupportsToolCall": true,
                "SupportsImages": false,
                "DescriptionZh": "腾讯混元 Turbo 大模型",
                "DescriptionEn": "Tencent Hunyuan Turbo",
                "Tags": [
                    "fast"
                ],
                "Clients": [
                    "WorkBuddy",
                    "CLI"
                ],
                "ServiceEndpoint": "https://hunyuan.tencentcloudapi.com",
                "Status": "ENABLED",
                "AgentCount": 3
            }
        ],
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

