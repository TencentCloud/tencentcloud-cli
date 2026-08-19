**Example 1: 按条件查询单副本SSD硬盘列表**

按状态过滤查询单副本SSD硬盘。

Input: 

```
tccli cbs DescribeRemoteDisks --cli-unfold-argument  \
    --Filters.0.Name remote-disk-state \
    --Filters.0.Values ATTACHED
```

Output: 
```
{
    "Response": {
        "RemoteDiskSet": [
            {
                "CreateTime": "2026-08-17T09:57:06+08:00",
                "DeadlineTime": "2026-10-17T18:11:09+08:00",
                "DiskChargeType": "PREPAID",
                "DiskSize": 2000,
                "InstanceId": "ins-1zmijkcu",
                "Placement": {
                    "CageId": "",
                    "CdcId": "",
                    "CdcName": "",
                    "DedicatedClusterId": "",
                    "ProjectId": 0,
                    "ProjectName": "",
                    "Zone": "ap-guangzhou-2"
                },
                "RemoteDiskId": "rdisk-80wdaldb",
                "RemoteDiskName": "未命名",
                "RemoteDiskState": "ATTACHED",
                "RemoteDiskType": "ELASTIC_REMOTE_SSD",
                "RenewFlag": "DISABLE_NOTIFY_AND_MANUAL_RENEW"
            }
        ],
        "TotalCount": 2,
        "RequestId": "55e81553-b057-4a64-8e63-590d84aa2d7f"
    }
}
```

**Example 2: 查询单副本SSD硬盘列表**



Input: 

```
tccli cbs DescribeRemoteDisks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RemoteDiskSet": [
            {
                "CreateTime": "2026-05-22T03:44:36+08:00",
                "DeadlineTime": "2026-06-22T11:44:36+08:00",
                "DiskChargeType": "PREPAID",
                "DiskSize": 3000,
                "InstanceId": "ins-kmmjtaxw",
                "Placement": {
                    "CageId": "",
                    "CdcId": "",
                    "CdcName": "",
                    "DedicatedClusterId": "",
                    "ProjectId": 0,
                    "ProjectName": "",
                    "Zone": "ap-guangzhou-2"
                },
                "RemoteDiskId": "rdisk-4idfknif",
                "RemoteDiskName": "未命名",
                "RemoteDiskState": "ATTACHED",
                "RemoteDiskType": "ELASTIC_REMOTE_SSD",
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW"
            }
        ],
        "TotalCount": 1,
        "RequestId": "b15edc0e-549d-4160-8796-78881ea55d48"
    }
}
```

