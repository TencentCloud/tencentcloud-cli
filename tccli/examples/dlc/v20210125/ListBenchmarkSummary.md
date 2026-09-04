**Example 1: 测试**



Input: 

```
tccli dlc ListBenchmarkSummary --cli-unfold-argument  \
    --Page 1 \
    --PageSize 50 \
    --StartTime 0 \
    --EndTime 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "BenchmarkCount": 4,
                "CreateTime": 1781247433444,
                "EndToEndAvg": 0,
                "EndToEndMedian": 0,
                "EndToEndP99": 0,
                "InputTokens": 256,
                "InterTokenLatencyAvg": 0,
                "InterTokenLatencyMedian": 0,
                "InterTokenLatencyP99": 0,
                "MaxConcurrency": 16,
                "ModelName": "qwen2.5",
                "ModelType": "LLM",
                "OutputTokens": 1024,
                "ParameterSize": "0.51B",
                "Provider": "personal",
                "RequestsPerSecond": 5,
                "ServiceName": "svc-cjl-3",
                "TaskName": "benchmark-svc-cjl-3-1781247433435",
                "TimePerOutputTokenAvg": 0,
                "TimePerOutputTokenMedian": 0,
                "TimePerOutputTokenP99": 0,
                "TimeToFirstTokenAvg": 0,
                "TimeToFirstTokenMedian": 0,
                "TimeToFirstTokenP99": 0
            }
        ],
        "Page": 1,
        "PageSize": 50,
        "Total": 2,
        "TotalPages": 1,
        "RequestId": "e4871813-b228-437d-b5e7-9339fb0980f2"
    }
}
```

