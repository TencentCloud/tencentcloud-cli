**Example 1: 查询请求汇总信息**



Input: 

```
tccli pts DescribeRequestSummary --cli-unfold-argument  \
    --JobId job-kufs4qhc \
    --ScenarioId scenario-ih54i7dm \
    --ProjectId project-pf8s0daq
```

Output: 
```
{
    "Response": {
        "RequestId": "abc-123-xyz",
        "RequestSummarySet": [
            {
                "Average": 0.0426436516818182,
                "Count": 25,
                "ErrorPercentage": 0,
                "Max": 0.077895098,
                "Method": "GET",
                "Min": 0.007491527,
                "P90": 0.08830936954286554,
                "P95": 0.09415468477143277,
                "P99": 0,
                "RPS": 1.8336389398233037,
                "Result": "",
                "Service": "http://mockhttpbin.pts.svc.cluster.local/get",
                "Status": ""
            }
        ]
    }
}
```

