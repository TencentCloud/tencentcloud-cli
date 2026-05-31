**Example 1: DescribeUsageRankList**



Input: 

```
tccli tokenhub DescribeUsageRankList --cli-unfold-argument  \
    --Dimension apikey \
    --StartTime 2026-04-09T00:00:00+08:00 \
    --EndTime 2026-05-09T00:00:00+08:00 \
    --Period 86400
```

Output: 
```
{
    "Response": {
        "Dimension": "apikey",
        "EndTime": "2026-05-09T00:00:00+08:00",
        "Limit": 0,
        "MetricKeys": [
            "TotalToken",
            "InputTotalToken",
            "OutputTotalToken"
        ],
        "MetricType": "tokens",
        "Offset": 0,
        "PageStats": {
            "InputTotalToken": 0,
            "OutputTotalToken": 0,
            "TotalToken": 0
        },
        "Period": 86400,
        "RequestId": "1568bc1c-946b-4c2b-b69f-6ba93f2bb258",
        "StartTime": "2026-04-09T00:00:00+08:00",
        "Timestamps": [],
        "TopList": [],
        "Total": 0,
        "TotalStats": {
            "InputTotalToken": 0,
            "OutputTotalToken": 0,
            "TotalToken": 0
        },
        "ViewName": "tokenhub_uin_apikeyid"
    }
}
```

