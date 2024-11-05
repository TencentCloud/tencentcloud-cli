**Example 1: 查询入侵防御放通封禁列表**

查询入侵防御放通封禁列表

Input: 

```
tccli cfw DescribeBlockIgnoreList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --SearchValue {"common":"模糊检索"} \
    --Direction 1 \
    --RuleType 1 \
    --Order desc \
    --By EndTime
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Action": 1,
                "Address": "土耳其伊斯坦布尔省伊斯坦布尔",
                "Comment": "阻断黑IP",
                "Country": "土耳其",
                "Direction": 1,
                "DirectionList": "1",
                "Domain": "www.domain.com",
                "EndTime": "2024-10-23 09:50:59",
                "EventName": "泛微OA蜜罐探测事件",
                "FwType": 15,
                "IP": "1.1.1.1",
                "IgnoreReason": "0",
                "Ioc": "1.1.1.1",
                "LastHitTime": "2024-10-21 16:59:09",
                "Level": "高危",
                "MatchTimes": 563038,
                "Protocol": "HTTP",
                "RuleType": 1,
                "Source": "网络蜜罐（严格模式）",
                "StartTime": "2024-09-27 09:50:59",
                "UniqueId": "appid-1.1.1.1-1-1"
            }
        ],
        "RequestId": "d4b7cab1-5594-41fb-88c6-67822af94807",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "RuleTypeDataList": [
            0,
            5,
            1,
            0,
            0,
            1,
            0
        ],
        "SourceList": [
            "基础防御",
            "手动添加",
            "网络蜜罐（严格模式）",
            "虚拟补丁"
        ],
        "Total": 30
    }
}
```

