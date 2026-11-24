**Example 1: 查询提示词模板摘要列表**



Input: 

```
tccli adp DescribePromptTemplateSummaryList --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 10 \
    --FilterList.0.Name PromptTemplateType \
    --FilterList.0.ValueList 1 \
    --IsFavorite False \
    --Query 质量 \
    --SpaceId default_space
```

Output: 
```
{
    "Response": {
        "PromptTemplateSummaryList": [
            {
                "IsFavorite": false,
                "LabelList": [
                    {
                        "Content": "任务执行",
                        "PromptTemplateLabelId": "2026568956095234048",
                        "PromptTemplateLabelType": 1
                    }
                ],
                "PermissionIdList": [
                    "adpPromptTemplateEdit"
                ],
                "Profile": {
                    "Audit": {
                        "CreateTime": "1778730485",
                        "Creator": "",
                        "CreatorName": "智能体开发平台",
                        "Operator": "",
                        "OperatorName": "",
                        "UpdateTime": "1778730485"
                    },
                    "Category": {
                        "Key": "PromptTemplateTypeBaselineEvaluation",
                        "Name": "基准评测"
                    },
                    "Description": "裁判模型在无参考答案情况下,根据回复质量打分。",
                    "Name": "按回复质量评分",
                    "PromptTemplateId": "2054770702757396480",
                    "PromptTemplateType": 1,
                    "SpaceId": "default_space"
                }
            }
        ],
        "TotalCount": 3,
        "RequestId": "efed2dc8-3f9b-427a-9f6e-e8f6b5898755"
    }
}
```

