**Example 1: 示例**



Input: 

```
tccli cwp DescribeScanState --cli-unfold-argument  \
    --ModuleType Vul
```

Output: 
```
{
    "Response": {
        "RiskEventCount": 1,
        "ScanEndTime": "2023-10-26 14:56:29",
        "Schedule": 1,
        "ScanState": 1,
        "ScanBeginTime": "2023-10-26 14:56:29",
        "RequestId": "c741a4fd-776f-499b-85a2-7bc70fd5b92s",
        "TaskId": 1,
        "VulId": [
            1
        ],
        "Type": 1
    }
}
```

