**Example 1: 获取示例问题**



Input: 

```
tccli wedata GetChatBiExampleQuestions --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --RoomKey 803627528827023360
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "UserConfigItems": [],
            "SystemConfigItems": [
                "简要总结空间内的数据和彼此的关联情况"
            ],
            "AiGenerateItems": [
                "请分析各城市的用户平均观影评分和票价敏感度关系。",
                "不同支付方式下，用户的评分分布和观影时段偏好有何差异？"
            ],
            "CanRefresh": true
        },
        "RequestId": "c92f1459-4d13-45ba-b891-65d461ed8b82"
    }
}
```

