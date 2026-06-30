**Example 1: 模型列表**



Input: 

```
tccli adp DescribeModelList --cli-unfold-argument  \
    --SpaceId default_space \
    --PageNumber 0 \
    --PageSize 24 \
    --Query youtu \
    --ModelScene 0 \
    --FilterList.0.Name DeveloperName \
    --FilterList.0.ValueList  \
    --FilterList.1.Name ProviderName \
    --FilterList.1.ValueList  \
    --FilterList.2.Name ProviderType \
    --FilterList.2.ValueList Self
```

Output: 
```
{
    "Response": {
        "ModelList": [
            {
                "BadgeList": [],
                "DeveloperInfo": {
                    "Alias": "腾讯优图",
                    "Name": "Youtu"
                },
                "LimitInfo": {
                    "ContextLengthDescription": "16K",
                    "InputLengthLimit": 12000,
                    "PromptLengthLimit": 4000
                },
                "ModelBasic": {
                    "Description": "针对企业知识问答场景精调训练，擅长多模态知识问答，适合图文表答案关联输出、数学计算、逻辑推理、表格问答等复杂场景有需求的场景。",
                    "IconUrl": "https://cdn.xiaowei.qq.com/adp/assets/youtu.png",
                    "ModelId": "Youtu/youtu-mrc-pro",
                    "ModelType": 1,
                    "Name": "youtu-mrc-pro"
                },
                "ParameterList": [
                    {
                        "DefaultValue": "0.6",
                        "EnumValueList": [],
                        "MaxValue": 1,
                        "MinValue": 0.1,
                        "Name": "top_p",
                        "Type": 1
                    },
                    {
                        "DefaultValue": "0.7",
                        "EnumValueList": [],
                        "MaxValue": 2,
                        "MinValue": 0,
                        "Name": "temperature",
                        "Type": 1
                    },
                    {
                        "DefaultValue": "4000",
                        "EnumValueList": [],
                        "MaxValue": 16000,
                        "MinValue": 1,
                        "Name": "max_tokens",
                        "Type": 2
                    }
                ],
                "PropertyList": [],
                "ProviderInfo": {
                    "Alias": "腾讯优图",
                    "Name": "Youtu",
                    "ProviderType": 1
                },
                "StatusInfo": {
                    "Concurrency": 0,
                    "IsExclusive": false,
                    "ResourceStatus": 0
                },
                "TagList": [
                    "文本推理"
                ]
            }
        ],
        "RequestId": "20fe36e6-1e65-45f6-a779-3d32886061f0",
        "TotalCount": 9
    }
}
```

