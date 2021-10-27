**Example 1: 查询日志**



Input: 

```
tccli cls GetAlarmLog --cli-unfold-argument  \
    --From 1608894763000 \
    --To 1608894763 \
    --Query ddddddddd \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "AnalysisRecords": [
            "xx"
        ],
        "Results": [
            {
                "PkgId": "xx",
                "TopicId": "xx",
                "FileName": "xx",
                "Source": "xx",
                "LogJson": "xx",
                "Time": 0,
                "TopicName": "xx",
                "PkgLogId": "xx"
            },
            {
                "PkgId": "xx",
                "TopicId": "xx",
                "FileName": "xx",
                "Source": "xx",
                "LogJson": "xx",
                "Time": 0,
                "TopicName": "xx",
                "PkgLogId": "xx"
            }
        ],
        "Analysis": true,
        "ListOver": false,
        "Context": "xx",
        "AnalysisResults": [
            {
                "Data": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ]
            },
            {
                "Data": [
                    {
                        "Key": "xx",
                        "Value": "xx"
                    }
                ]
            },
            {
                "Data": [
                    {
                        "Key": "xx",
                        "Value": "xx"
                    }
                ]
            }
        ],
        "ColNames": [
            "time",
            "pv",
            "uv"
        ],
        "Columns": [
            {
                "Type": "xx",
                "Name": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

