**Example 1: 示例**



Input: 

```
tccli cwp DescribeScanTaskDetails --cli-unfold-argument  \
    --ModuleType Vul \
    --TaskId 1
```

Output: 
```
{
    "Response": {
        "ScanContent": [
            "xx"
        ],
        "VulInfo": [
            {
                "CveId": "xx",
                "CvssScore": 0.0,
                "Name": "xx",
                "Reference": "xx",
                "Level": 1,
                "Fix": "xx",
                "Descript": "xx",
                "PublishTime": "xx",
                "VulId": 1,
                "Cvss": "xx",
                "VulCategory": 1
            }
        ],
        "ScanMachineCount": 1,
        "ScanTaskDetailList": [
            {
                "Status": "xx",
                "Uuid": "xx",
                "ScanEndTime": "xx",
                "FailType": 1,
                "HostName": "xx",
                "ScanBeginTime": "xx",
                "OsName": "xx",
                "Quuid": "xx",
                "HostIp": "xx",
                "RiskNum": 1,
                "Id": 1,
                "Description": "xx"
            }
        ],
        "ScanEndTime": "xx",
        "ScanTime": 1,
        "ScanProgress": 1,
        "ScanLeftTime": 1,
        "ScanBeginTime": "xx",
        "TotalCount": 1,
        "RequestId": "xx",
        "RiskEventCount": 1,
        "VulCount": 1,
        "RiskMachineCount": 1,
        "Type": 1,
        "StoppingAll": false
    }
}
```

