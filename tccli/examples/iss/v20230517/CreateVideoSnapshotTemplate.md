**Example 1: 成功**

实时截帧模板创建

Input: 

```
tccli iss CreateVideoSnapshotTemplate --cli-unfold-argument  \
    --Name 实时截帧模板 \
    --Type 1 \
    --Interval 120 \
    --Times.0.BeginTime 9:00:00 \
    --Times.0.EndTime 12:00:00 \
    --Times.0.WeekDay 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": "2026-01-25 12:10:49",
            "Interval": 120,
            "MultiMode": {
                "Enable": false,
                "Interval": 0,
                "Total": 0
            },
            "Name": "实时截帧模板",
            "TemplateId": "b11*********e*******************48c4",
            "Times": [
                {
                    "BeginTime": "9:00:00",
                    "EndTime": "12:00:00",
                    "WeekDay": 1
                }
            ],
            "Type": 1,
            "UpdateTime": "2026-01-25 12:10:49"
        },
        "RequestId": "c8453e1b-2428-4ec3-bfee-3b6412b41de6"
    }
}
```

