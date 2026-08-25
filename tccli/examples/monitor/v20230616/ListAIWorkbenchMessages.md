**Example 1: 按顺序获取历史会话**



Input: 

```
tccli monitor ListAIWorkbenchMessages --cli-unfold-argument  \
    --SessionId ses-************ \
    --Cursor ent-************
```

Output: 
```
{
    "Response": {
        "HasMore": false,
        "Messages": [
            {
                "Content": "根据查询结果，最近三天（2023年10月18日至2023年10月20日）内没有云服务器的告警历史记录。这可能意味着：\n\n1. **系统运行正常**：云服务器在此期间未触发任何告警。\n2. **告警策略未配置**：可能未设置相关告警策略，导致未捕获异常情况。\n3. **数据延迟或未上报**：告警数据可能存在延迟或未及时上报。\n\n如果需要进一步确认，可以检查告警策略配置或扩大时间范围重新查询。",
                "ContentBlocks": [
                    {
                        "Data": "{\"messageId\":\"ent-v05jrikcax7p\",\"role\":\"assistant\",\"timestamp\":1775800599000,\"type\":\"TEXT_MESSAGE_START\"}",
                        "Type": "TEXT_MESSAGE_START"
                    }
                ],
                "EntryId": "ent-v05jrikcax7p",
                "Role": "assistant",
                "SessionId": "ses-ddgf8e7ne7ak",
                "Status": "completed"
            }
        ],
        "NextCursor": "ent-************",
        "RequestId": "0c3f9c3a-fac9-40b9-8249-79eb32271c4a"
    }
}
```

