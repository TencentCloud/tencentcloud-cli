**Example 1: 查询独享集群详情**

查询独享集群dbdc-dq8w02u5详情信息

Input: 

```
tccli dbdc DescribeInstanceDetail --cli-unfold-argument  \
    --InstanceId dbdc-dq8w02u5
```

Output: 
```
{
    "Response": {
        "AssignStrategy": 1,
        "AutoRenewFlag": 1,
        "ClusterId": "devtest",
        "CpuAssignable": 64,
        "CpuAssigned": 0,
        "CpuSpec": 64,
        "CreateTime": "2025-05-19 16:12:02",
        "DbNum": 0,
        "DiskAssignable": 10500,
        "DiskAssigned": -12,
        "DiskSpec": 14000,
        "FenceId": "",
        "HostNum": 2,
        "HostType": 0,
        "InstanceId": "dbdc-dq8w02u5",
        "InstanceName": "ankersong",
        "MemoryAssignable": 192,
        "MemoryAssigned": -2,
        "MemorySpec": 256,
        "PeriodEndTime": "2025-06-19 16:12:02",
        "ProductId": 1,
        "Region": "ap-guangzhou",
        "RequestId": "5a4e4e6b-f7a8-4494-92c1-a5adbcb8e656",
        "ResourceTags": [],
        "Status": 1,
        "StatusDesc": "运行中",
        "Type": 0,
        "Zone": "ap-guangzhou-2",
        "CpuType": "Intel/AMD"
    }
}
```

