**Example 1: 成功**



Input: 

```
tccli iss DescribeVideoSnapshotTemplate --cli-unfold-argument  \
    --TemplateId 144*****************************f3d3
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": "2026-01-25 11:52:57",
            "Interval": 120,
            "MultiMode": {
                "Enable": false,
                "Interval": 0,
                "Total": 0
            },
            "Name": "实时截帧模板",
            "TemplateId": "144*****************************f3d3",
            "Times": [
                {
                    "BeginTime": "9:00:00",
                    "EndTime": "12:00:00",
                    "WeekDay": 1
                }
            ],
            "Type": 1,
            "UpdateTime": "2026-01-25 11:52:57"
        },
        "RequestId": "3cc0e68c-58eb-46a0-93d9-a3b749d30a74"
    }
}
```

