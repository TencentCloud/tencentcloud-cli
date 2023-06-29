**Example 1: 请求示例DEMO**



Input: 

```
tccli dbdc DescribeInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "Instances": [
            {
                "InstanceStatus": 0,
                "Zone": "xx",
                "InstanceId": "xx",
                "Region": "xx",
                "Pid": 10875,
                "CreateTime": "xx",
                "Machine": "xx",
                "AutoRenewFlag": 0,
                "InstanceDetail": {
                    "Status": 0,
                    "ReadWriteTotalMemory": 1,
                    "ReadWriteTotalLeaveMemory": 1,
                    "ReadWriteTotalLeaveDisk": 1,
                    "ReadOnlyTotalLeaveDisk": 1,
                    "ReadOnlyTotalMemory": 1,
                    "ReadOnlyTotalLeaveMemory": 1,
                    "ReadOnlyTotalDisk": 1,
                    "InstanceDeviceInfos": [
                        {
                            "InstanceId": "xx",
                            "FreeDevice": [
                                {
                                    "RawDeviceNum": 1,
                                    "InstanceNum": 1,
                                    "DevClass": "xx",
                                    "RestDisk": 1,
                                    "DeviceId": 0,
                                    "DeviceNo": "xx",
                                    "MaxDisk": 1
                                }
                            ],
                            "ReadWriteDevice": [
                                {
                                    "RawDeviceNum": 1,
                                    "InstanceNum": 1,
                                    "DevClass": "xx",
                                    "RestDisk": 1,
                                    "DeviceId": 0,
                                    "DeviceNo": "xx",
                                    "MaxDisk": 1
                                }
                            ],
                            "ReadOnlyDevice": [
                                {
                                    "RawDeviceNum": 1,
                                    "InstanceNum": 1,
                                    "DevClass": "xx",
                                    "RestDisk": 1,
                                    "DeviceId": 0,
                                    "DeviceNo": "xx",
                                    "MaxDisk": 1
                                }
                            ]
                        }
                    ],
                    "ReadWriteTotalDisk": 1
                },
                "AppId": 1,
                "PeriodEndTime": "xx",
                "InstanceName": "xx",
                "InstanceType": 0
            },
            {
                "InstanceStatus": 0,
                "Zone": "xx",
                "InstanceId": "xx",
                "Region": "xx",
                "Pid": 10875,
                "InstanceType": 0,
                "Machine": "xx",
                "AutoRenewFlag": 0,
                "InstanceDetail": {
                    "Status": 0,
                    "ReadWriteTotalMemory": 1,
                    "ReadWriteTotalLeaveMemory": 1,
                    "ReadWriteTotalLeaveDisk": 1,
                    "ReadOnlyTotalLeaveDisk": 1,
                    "ReadOnlyTotalMemory": 1,
                    "ReadOnlyTotalLeaveMemory": 1,
                    "ReadOnlyTotalDisk": 1,
                    "InstanceDeviceInfos": [
                        {
                            "InstanceId": "xx",
                            "FreeDevice": [
                                {
                                    "RawDeviceNum": 1,
                                    "InstanceNum": 1,
                                    "DevClass": "xx",
                                    "RestDisk": 1,
                                    "DeviceId": 0,
                                    "DeviceNo": "xx",
                                    "MaxDisk": 1
                                }
                            ],
                            "ReadWriteDevice": [
                                {
                                    "RawDeviceNum": 1,
                                    "InstanceNum": 1,
                                    "DevClass": "xx",
                                    "RestDisk": 1,
                                    "DeviceId": 0,
                                    "DeviceNo": "xx",
                                    "MaxDisk": 1
                                }
                            ],
                            "ReadOnlyDevice": [
                                {
                                    "RawDeviceNum": 1,
                                    "InstanceNum": 1,
                                    "DevClass": "xx",
                                    "RestDisk": 1,
                                    "DeviceId": 0,
                                    "DeviceNo": "xx",
                                    "MaxDisk": 1
                                }
                            ]
                        }
                    ],
                    "ReadWriteTotalDisk": 1
                },
                "AppId": 1,
                "PeriodEndTime": "xx",
                "InstanceName": "xx",
                "CreateTime": "xx"
            }
        ]
    }
}
```

