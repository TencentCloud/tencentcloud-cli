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
                "SupportsThinking": false,
                "ThinkingLevels": [],
                "DefaultThinkingLevel": "",
                "CanDisableThinking": false,
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

**Example 2: 按模型 ID 查询思考能力**

按模型 ID 精确查询单个模型的思考能力。ThinkingLevels 为大写枚举，在 Agent 版本 Manifest 中配置 thinking.level 时取小写（如 LOW 对应 low）。该模型 CanDisableThinking 为 false，不提供关闭思考的选项。

Input: 

```
tccli workbuddyenterprise DescribeBuiltinModelList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --Filters.0.Name ModelId \
    --Filters.0.Values hy3 \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "BuiltinModelSet": [
            {
                "ModelId": "hy3",
                "Name": "Hy3",
                "Vendor": "TENCENT",
                "MaxOutputTokens": 64000,
                "MaxInputTokens": 192000,
                "SupportsToolCall": true,
                "SupportsImages": true,
                "SupportsThinking": true,
                "ThinkingLevels": [
                    "LOW",
                    "HIGH"
                ],
                "DefaultThinkingLevel": "HIGH",
                "CanDisableThinking": false,
                "DescriptionZh": "混元思考模型，具有增强的推理能力",
                "DescriptionEn": "Hunyuan's thinking model with enhanced reasoning capabilities",
                "Tags": [
                    "craft"
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
        "RequestId": "7a1e5f20-2468-4ace-8bdf-13579bdf2468"
    }
}
```

