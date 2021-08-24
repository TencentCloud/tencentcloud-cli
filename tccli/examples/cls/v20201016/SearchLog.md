**Example 1: 查询日志**



Input: 

```
tccli cls SearchLog --cli-unfold-argument  \
    --TopicId 682d0718-07bb-4ec0-9fda-f1e9a2767e0b \
    --From 1608794854000 \
    --To 1608794855000 \
    --Query http_status:200 \
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
                "Time": 1608794854001,
                "TopicName": "xx",
                "PkgLogId": "xx"
            }
        ],
        "Analysis": false,
        "ListOver": true,
        "Context": "xx",
        "AnalysisResults": [
            {
                "Data": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ]
            }
        ],
        "ColNames": [
            "xx"
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

