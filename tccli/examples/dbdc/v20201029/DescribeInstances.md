**Example 1: 请求示例DEMO**



Input: 

```
tccli dbdc DescribeInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "AppId": 1252328453,
                "AutoRenewFlag": 0,
                "CreateTime": "2021-02-25T16:08:47+08:00",
                "InstanceDetail": {
                    "InstanceDeviceInfos": [
                        {
                            "FreeDevice": [],
                            "InstanceId": "szjr-3-7",
                            "ReadOnlyDevice": [],
                            "ReadWriteDevice": [
                                {
                                    "DevClass": "SH12",
                                    "DeviceId": 191108504,
                                    "DeviceNo": "",
                                    "InstanceNum": 29,
                                    "MaxDisk": 28000,
                                    "MaxMemory": 576,
                                    "RawDeviceNum": 3,
                                    "RestDisk": 8800,
                                    "RestMemory": 248
                                }
                            ]
                        }
                    ],
                    "ReadOnlyTotalDisk": 0,
                    "ReadOnlyTotalLeaveDisk": 0,
                    "ReadOnlyTotalLeaveMemory": 0,
                    "ReadOnlyTotalMemory": 0,
                    "ReadWriteTotalDisk": 28000,
                    "ReadWriteTotalLeaveDisk": 8800,
                    "ReadWriteTotalLeaveMemory": 248,
                    "ReadWriteTotalMemory": 576,
                    "Status": 0
                },
                "InstanceId": "dbdc-qhdgwfs",
                "InstanceName": "exclust",
                "InstanceStatus": 1,
                "InstanceType": 1,
                "Machine": "SH12",
                "PeriodEndTime": "2021-09-25T16:08:47+08:00",
                "Pid": 10875,
                "Region": "ap-shenzhen-fsi",
                "Zone": "ap-shenzhen-fsi-3"
            }
        ],
        "RequestId": "d82b7fa2-090c-4cf6-aefe-376510cebd81",
        "TotalCount": 1
    }
}
```

