**Example 1: 查询主机列表**



Input: 

```
tccli dbdc DescribeHostList --cli-unfold-argument  \
    --InstanceId dbdc-test
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "Hosts": [
            {
                "Status": 1,
                "DbNum": 0,
                "DiskSpec": 6000,
                "Zone": "ap-guangzhou-1",
                "CpuAssignable": 32,
                "DiskAssignable": 3000,
                "DiskAssigned": 0,
                "AssignStatus": 0,
                "HostType": 0,
                "DiskRatio": 0.5,
                "CpuSpec": 32,
                "MemoryAssigned": 0,
                "HostId": "svr-kbpiagjd",
                "MemoryAssignable": 128,
                "MemorySpec": 128,
                "HostName": "svr-kbpiagjd",
                "MemoryRatio": 1,
                "CpuRatio": 1,
                "CpuAssigned": 0,
                "MachineName": "HYI12A",
                "MachineType": "SH12",
                "PidTag": "excluster_xxx",
                "Pid": 10811
            },
            {
                "Status": 1,
                "DbNum": 0,
                "DiskSpec": 6000,
                "Zone": "ap-guangzhou-1",
                "CpuAssignable": 32,
                "DiskAssignable": 3000,
                "DiskAssigned": 0,
                "AssignStatus": 0,
                "HostType": 0,
                "DiskRatio": 0.5,
                "CpuSpec": 32,
                "MemoryAssigned": 0,
                "HostId": "svr-7oefkrrn",
                "MemoryAssignable": 128,
                "MemorySpec": 128,
                "HostName": "svr-7oefkrrn",
                "MemoryRatio": 1,
                "CpuRatio": 1,
                "CpuAssigned": 0,
                "MachineName": "HYI12A",
                "MachineType": "SH12",
                "PidTag": "excluster_xxx",
                "Pid": 10811
            }
        ],
        "RequestId": "58520b56-b1ff-11eb-90cd-525400542aa6"
    }
}
```

