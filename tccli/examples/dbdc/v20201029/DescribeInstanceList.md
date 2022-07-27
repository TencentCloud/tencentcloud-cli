**Example 1: 查询独享集群接口列表**



Input: 

```
tccli dbdc DescribeInstanceList --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0 \
    --OrderBy createTime \
    --SortBy desc
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
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
        ],
        "RequestId": "8cf4daa6-b172-11eb-94d3-525400542aa6",
        "TotalCount": 1
    }
}
```

