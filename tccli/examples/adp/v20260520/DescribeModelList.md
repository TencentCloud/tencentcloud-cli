**Example 1: 查询模型列表**



Input: 

```
tccli adp DescribeModelList --cli-unfold-argument  \
    --ModelScene 1 \
    --SpaceId default_space
```

Output: 
```
{
    "Response": {
        "ModelList": [
            {
                "ModelBasic": {
                    "ModelId": "DeepSeek-V3.2",
                    "Name": "DeepSeek-V3.2",
                    "Description": "通用大语言模型",
                    "IconUrl": "https://example.cos.ap-guangzhou.myqcloud.com/public/adp/model-icon/deepseek.png",
                    "ModelType": 1
                },
                "ProviderInfo": {
                    "Name": "deepseek",
                    "Alias": "DeepSeek",
                    "ProviderType": 1
                },
                "LimitInfo": {
                    "ContextLengthDescription": "128K",
                    "InputLengthLimit": 8000,
                    "PromptLengthLimit": 4000
                },
                "StatusInfo": {
                    "ResourceStatus": 1,
                    "IsExclusive": false,
                    "Concurrency": 0
                },
                "ParameterList": [
                    {
                        "Name": "temperature",
                        "Type": 1,
                        "DefaultValue": "0.7",
                        "MinValue": 0,
                        "MaxValue": 1,
                        "EnumValueList": []
                    }
                ],
                "PropertyList": [
                    {
                        "Name": "support_workflow_status",
                        "Value": "1"
                    }
                ],
                "TagList": [
                    "generate"
                ],
                "BadgeList": []
            }
        ],
        "RequestId": "d8712288-6b1d-4e94-9f5a-77904d3cd2df"
    }
}
```

