**Example 1: 获取告警屏蔽配置信息**

获取告警屏蔽配置信息

Input: 

```
tccli cls DescribeAlarmShields --cli-unfold-argument  \
    --AlarmNoticeId notice-ea115e5a-04c4-421e-9ba3-fb177e9025cb \
    --Filters.0.Key status \
    --Filters.0.Values 1 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AlarmShields": [
            {
                "AlarmNoticeId": "notice-ea115e5a-04c4-421e-9ba3-fb177e9025cb",
                "TaskId": "ea115e5a-04c4-421e-9ba3-fb177e9025cb",
                "StartTime": 1701933943,
                "EndTime": 1701993943,
                "Type": 1,
                "Rule": "",
                "Reason": "系统发布，暂时屏蔽",
                "Source": 1,
                "Operator": "1001（张三）",
                "Status": 1,
                "CreateTime": 1701933943,
                "UpdateTime": 1701933943
            }
        ],
        "RequestId": "11115e5a-04c4-421e-9ba3-fb177e902511"
    }
}
```

