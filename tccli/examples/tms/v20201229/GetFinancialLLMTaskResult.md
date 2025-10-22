**Example 1: 获取金融大模型审校任务结果：示例**



Input: 

```
tccli tms GetFinancialLLMTaskResult --cli-unfold-argument  \
    --TaskId 17719984-030f-4b32-8828-61d3c21b3324
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "Label": "违规荐股荐基",
                "Reasons": [
                    {
                        "Reason": "复核发现主审核模型误判。原审核认为 ...",
                        "TargetText": "2008年股市低迷..."
                    }
                ],
                "Suggestion": "Block"
            }
        ],
        "RequestId": "4b180195-fe4b-4fa1-8e12-536054fbde27",
        "ReviewedLabels": [
            "宏观走势造谣",
            "数据来源缺失",
            "违规荐股荐基"
        ],
        "StartTime": "2025-09-25 19:42:35",
        "Status": "Success"
    }
}
```

