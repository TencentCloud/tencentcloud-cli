**Example 1: 获取内容安全识别按天统计结果明细**

显示内容安全识别趋势图

Input: 

```
tccli cms DescribeModerationDetailsPlatform --cli-unfold-argument  \
    --OrderBy abc \
    --EndDate 2020-09-22 \
    --BeginDate 2020-09-22 \
    --CustomUin abc \
    --CustomSubAccountUin abc \
    --Limit 0 \
    --OrderField abc \
    --Offset 0 \
    --CustomAppId abc \
    --Channel 0 \
    --Filters.0.Name abc \
    --Filters.0.Values abc
```

Output: 
```
{
    "Response": {
        "RequestId": "90f4d3cc-02be-4875-a708-fbca7865b73e",
        "Results": {
            "TotalCount": 4,
            "Data": [
                {
                    "Date": "20190616",
                    "ServiceType": "Image",
                    "Counts": [
                        {
                            "EvilType": 100,
                            "Count": 2633,
                            "Duration": 0
                        }
                    ]
                },
                {
                    "Date": "20190615",
                    "ServiceType": "Image",
                    "Counts": [
                        {
                            "EvilType": 20001,
                            "Count": 1,
                            "Duration": 0
                        }
                    ]
                },
                {
                    "Date": "20190614",
                    "ServiceType": "Audio",
                    "Counts": [
                        {
                            "EvilType": 20001,
                            "Count": 4963,
                            "Duration": 2157
                        },
                        {
                            "EvilType": 20002,
                            "Count": 7,
                            "Duration": 4
                        }
                    ]
                },
                {
                    "Date": "20190614",
                    "ServiceType": "Image",
                    "Counts": [
                        {
                            "EvilType": 20001,
                            "Count": 4856,
                            "Duration": 0
                        },
                        {
                            "EvilType": 20002,
                            "Count": 7,
                            "Duration": 0
                        },
                        {
                            "EvilType": 20006,
                            "Count": 4960,
                            "Duration": 0
                        },
                        {
                            "EvilType": 20103,
                            "Count": 16,
                            "Duration": 0
                        },
                        {
                            "EvilType": 24001,
                            "Count": 4869,
                            "Duration": 0
                        },
                        {
                            "EvilType": 100,
                            "Count": 334,
                            "Duration": 0
                        }
                    ]
                }
            ]
        }
    },
    "retcode": 0,
    "retmsg": "success"
}
```

