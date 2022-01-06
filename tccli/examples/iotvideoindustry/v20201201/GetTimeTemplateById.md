**Example 1: 根据模板ID获取时间模板**



Input: 

```
tccli iotvideoindustry GetTimeTemplateById --cli-unfold-argument  \
    --TemplateId tgrp-xxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8",
        "Template": {
            "TemplateId": "tgrp-xxxxxxx",
            "Name": "xxx",
            "IsAllWeek": 0,
            "Type": 1,
            "TimeTemplateSpecs": [
                {
                    "DayofWeek": 2,
                    "BeginTime": "10:30",
                    "EndTime": "15:30"
                }
            ]
        }
    }
}
```

