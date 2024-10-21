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
            "cve"
        ],
        "VulInfo": [
            {
                "CveId": "cve-xx",
                "CvssScore": 0,
                "Name": "name",
                "Reference": "ref",
                "Level": 1,
                "Fix": "fix",
                "Descript": "desc",
                "PublishTime": " 2019-12-25 11:57:15",
                "VulId": 1,
                "Cvss": "cvss",
                "VulCategory": 1
            }
        ],
        "ScanMachineCount": 1,
        "ScanTaskDetailList": [
            {
                "Status": "status",
                "Uuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "ScanEndTime": " 2019-12-25 11:57:15",
                "FailType": 1,
                "HostName": "hostname",
                "ScanBeginTime": " 2019-12-25 11:57:15",
                "OsName": "osname",
                "Quuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "HostIp": "xx.xx.xx.xx",
                "RiskNum": 1,
                "Id": 1,
                "Description": "desc",
                "MachineWanIp": "xx.xx.xx.xx",
                "MachineExtraInfo": {
                    "WanIP": "xx.xx.xx.xx",
                    "PrivateIP": "xx.xx.xx.xx",
                    "NetworkType": 0,
                    "NetworkName": "name",
                    "InstanceID": "ins-xxx",
                    "HostName": "hostname"
                }
            }
        ],
        "ScanEndTime": " 2019-12-25 11:57:15",
        "ScanTime": 1,
        "ScanProgress": 1,
        "ScanLeftTime": 1,
        "ScanBeginTime": " 2019-12-25 11:57:15",
        "TotalCount": 1,
        "RequestId": "xxxxxxxx-1234-5678-9101-yyyyyyyyyy",
        "RiskEventCount": 1,
        "VulCount": 1,
        "RiskMachineCount": 1,
        "Type": 1,
        "StoppingAll": false
    }
}
```

