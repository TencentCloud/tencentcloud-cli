**Example 1: 用例1**



Input: 

```
tccli adp DescribeMsgRecordList --cli-unfold-argument  \
    --AppId 2087429578337166592 \
    --FilterList.0.Name StartTime \
    --FilterList.0.ValueList 1786118400
```

Output: 
```
{
    "Response": {
        "HasMore": false,
        "MsgRecordList": [
            {
                "Answer": "# 《逆天仙途》\n\n## 第一章：废柴逆命\n\n---\n\n苍莽山脉深处，云雾缭绕如海。\n\n落云城外，一座破旧的柴房内，少年林渊盘膝而坐，双目紧闭，额上青筋暴起，豆大的汗珠顺着脸颊滚落。\n\n\"又失败了。\"\n\n他缓缓睁开眼，眸中满是苦涩。十六岁，练",
                "AppId": "2087429578337166592",
                "CategoryId": "0",
                "CreateTime": "1786526009",
                "Intent": "其他问题",
                "IntentCategory": "default",
                "IsSmart": false,
                "Question": "帮我写一个修仙小说 不调用任何工具",
                "RecordId": "Gwx_20260812_171328_602_BAZ2vswt",
                "ReplyMethod": 10,
                "Result": {
                    "CallResult": 3,
                    "CustomerVariable": "**",
                    "FailReason": "0",
                    "FirstTokenLatency": 2685,
                    "InputToken": 1991,
                    "OutputToken": 44,
                    "TotalToken": 2035,
                    "TotalTokenLatency": 6444
                },
                "Score": 0,
                "SessionId": "c0a10dbb-b9fa-4aae-89fd-7f0d44a8eec0",
                "Source": {
                    "ChannelType": 2,
                    "FromId": "1319",
                    "FromType": 2,
                    "UserAvatar": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/avatar_sheep01.png",
                    "UserId": "1932008810606356480",
                    "UserNickname": "ty_02@tt.com"
                },
                "TraceId": "34e89fa8029842ebaaac03cd31192d23"
            }
        ],
        "NextCursor": "{\"cursor_time\":\"2026-08-12 14:43:24\",\"skipped\":6}",
        "PrevCursor": "{\"cursor_time\":\"2026-08-12 17:13:29\",\"skipped\":0}",
        "TotalCount": "6",
        "RequestId": "b3eedba2-e542-4e7e-aa84-0b2d46f8ec1f"
    }
}
```

