**Example 1: 获取智能编辑任务结果**



Input: 

```
tccli ie DescribeEditingTaskResult --cli-unfold-argument  \
    --TaskId 8E312055EBF7A503B92947E6D3B21EFF_1573715265075
```

Output: 
```
{
    "Response": {
        "TaskResult": {
            "TaskId": "8E312055EBF7A503B92947E6D3B21EFF_1573715265075",
            "Status": 2,
            "TagTaskResult": {
                "Status": 2,
                "ErrCode": 0,
                "ErrMsg": "Success.",
                "ItemSet": [
                    {
                        "Tag": "动画片",
                        "Confidence": 90.17
                    }
                ]
            },
            "ClassificationTaskResult": null,
            "StripTaskResult": null,
            "HighlightsTaskResult": null,
            "CoverTaskResult": null,
            "OpeningEndingTaskResult": null
        },
        "RequestId": "5d199208-24c9-44a3-ab55-192ff22207c9"
    }
}
```

