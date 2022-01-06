**Example 1: 获取时间模板列表**



Input: 

```
tccli iotvideoindustry GetTimeTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "f8375a13-7189-42f2-93f7-1aaca6eaf25d",
        "Templates": [
            {
                "TemplateId": "tgrp-jfs89ahg",
                "Name": "全天候模板",
                "IsAllWeek": 1,
                "Type": 0,
                "TimeTemplateSpecs": []
            },
            {
                "TemplateId": "tgrp-fmwq1f1a",
                "Name": "工作日模板",
                "IsAllWeek": 0,
                "Type": 0,
                "TimeTemplateSpecs": [
                    {
                        "DayofWeek": 1,
                        "BeginTime": "00:00",
                        "EndTime": "23:59"
                    },
                    {
                        "DayofWeek": 2,
                        "BeginTime": "00:00",
                        "EndTime": "23:59"
                    },
                    {
                        "DayofWeek": 3,
                        "BeginTime": "00:00",
                        "EndTime": "23:59"
                    },
                    {
                        "DayofWeek": 4,
                        "BeginTime": "00:00",
                        "EndTime": "23:59"
                    },
                    {
                        "DayofWeek": 5,
                        "BeginTime": "00:00",
                        "EndTime": "23:59"
                    }
                ]
            },
            {
                "TemplateId": "tgrp-ttcqknio",
                "Name": "周末模板",
                "IsAllWeek": 0,
                "Type": 0,
                "TimeTemplateSpecs": [
                    {
                        "DayofWeek": 6,
                        "BeginTime": "00:00",
                        "EndTime": "23:59"
                    },
                    {
                        "DayofWeek": 7,
                        "BeginTime": "00:00",
                        "EndTime": "23:59"
                    }
                ]
            },
            {
                "TemplateId": "tgrp-qfr07ro5",
                "Name": "xx",
                "IsAllWeek": 1,
                "Type": 1,
                "TimeTemplateSpecs": []
            },
            {
                "TemplateId": "tgrp-712kfd0s",
                "Name": "xx",
                "IsAllWeek": 1,
                "Type": 1,
                "TimeTemplateSpecs": []
            },
            {
                "TemplateId": "tgrp-a6gvpkzu",
                "Name": "xx",
                "IsAllWeek": 1,
                "Type": 1,
                "TimeTemplateSpecs": []
            }
        ],
        "TotalCount": 6
    }
}
```

