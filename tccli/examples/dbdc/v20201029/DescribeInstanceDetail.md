**Example 1: 查询独享集群详情**



Input: 

```
tccli dbdc DescribeInstanceDetail --cli-unfold-argument  \
    --InstanceId dbdc-test
```

Output: 
```
{
    "Response": {
        "RequestId": "22cb8292-b16d-11eb-8d13-525400542aa6",
        "DbNum": 0,
        "CpuAssignable": 64,
        "HostType": 0,
        "AutoRenewFlag": 0,
        "Type": 0,
        "Status": 1,
        "InstanceId": "dbdc-test",
        "AssignStrategy": 0,
        "PeriodEndTime": "2021-05-28 00:00:00",
        "HostNum": 2,
        "MemoryAssignable": 256,
        "CpuSpec": 64,
        "DiskSpec": 12000,
        "MemorySpec": 256,
        "MemoryAssigned": 0,
        "StatusDesc": "运行中",
        "InstanceName": "test",
        "CpuAssigned": 0,
        "ProductId": 1,
        "DiskAssignable": 6000,
        "DiskAssigned": 0,
        "Region": "ap-guangzhou",
        "Zone": "ap-guangzhou-3",
        "FenceId": "cage-x-x",
        "ClusterId": "",
        "CreateTime": "2021-04-28 00:00:00"
    }
}
```

