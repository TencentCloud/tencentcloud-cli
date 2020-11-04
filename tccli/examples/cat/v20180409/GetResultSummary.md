**Example 1: 获取任务列表的实时数据**



Input: 

```
tccli cat GetResultSummary --cli-unfold-argument  \
    --TaskIds 226791
```

Output: 
```
{
    "Response": {
        "RealData": [
            {
                "LogTime": "2019-12-12 21:29:00",
                "TaskId": 242730,
                "AvailRatio": 100,
                "ReponseTime": 193.63
            },
            {
                "LogTime": "2019-12-12 21:29:00",
                "TaskId": 242789,
                "AvailRatio": 92.31,
                "ReponseTime": 1116.65
            },
            {
                "LogTime": "2019-12-12 21:29:00",
                "TaskId": 242791,
                "AvailRatio": 100,
                "ReponseTime": 679.82
            },
            {
                "LogTime": "2019-12-12 21:29:00",
                "TaskId": 242792,
                "AvailRatio": 100,
                "ReponseTime": 112.31
            }
        ],
        "DayData": [
            {
                "LogTime": "2019-12-12 00:00:00",
                "TaskId": 242730,
                "AvailRatio": 100,
                "ReponseTime": 225.31
            },
            {
                "LogTime": "2019-12-12 00:00:00",
                "TaskId": 242789,
                "AvailRatio": 98.04,
                "ReponseTime": 841.64
            },
            {
                "LogTime": "2019-12-12 00:00:00",
                "TaskId": 242791,
                "AvailRatio": 98.77,
                "ReponseTime": 672.66
            },
            {
                "LogTime": "2019-12-12 00:00:00",
                "TaskId": 242792,
                "AvailRatio": 100,
                "ReponseTime": 80.06
            }
        ],
        "RequestId": "a7be32f9-4e5c-4996-8cc9-15a2d11055d8"
    }
}
```

