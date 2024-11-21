**Example 1: 查询所有已挂载的数据盘**

用于查询所有已挂载的数据盘

Input: 

```
tccli cbs DescribeDisks --cli-unfold-argument  \
    --Filters.0.Values ATTACHED \
    --Filters.0.Name disk-state \
    --Filters.1.Values DATA_DISK \
    --Filters.1.Name disk-usage
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "e2386a23-48c1-4c18-9a36-4e7354f333b2",
        "DiskSet": [
            {
                "DeleteWithInstance": false,
                "Encrypt": false,
                "DiskType": "CLOUD_BSSD",
                "AutoRenewFlagError": false,
                "Rollbacking": false,
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "DiskName": "my-data-disk",
                "Tags": [],
                "InstanceId": "",
                "DifferDaysOfDeadline": 1,
                "DiskId": "disk-b94t5dzt",
                "DiskState": "ATTACHED",
                "Placement": {
                    "ProjectId": 0,
                    "Zone": "ap-guangzhou-2",
                    "ProjectName": "默认项目",
                    "CageId": "cage-bdq5l1mx",
                    "CdcName": "my-cloud-dedicated-cbs",
                    "CdcId": "cdc-1648zauv",
                    "DedicatedClusterId": "cluster-o42khj98"
                },
                "IsReturnable": false,
                "DeadlineTime": "2018-10-26 10:55:43",
                "Attached": true,
                "DiskSize": 10,
                "DiskUsage": "DATA_DISK",
                "Portable": true,
                "DiskChargeType": "PREPAID",
                "SnapshotAbility": true,
                "DeadlineError": false,
                "RollbackPercent": 100,
                "AutoSnapshotPolicyIds": null,
                "ReturnFailCode": 3,
                "CreateTime": "2018-09-26 17:36:07",
                "ThroughputPerformance": 1,
                "Migrating": true,
                "InstanceIdList": [
                    "ins-agp4l0lx"
                ],
                "Shareable": true,
                "MigratePercent": 100,
                "SnapshotSize": 100,
                "SnapshotCount": 0,
                "BackupDisk": true,
                "AttachMode": "PF",
                "DiskBackupQuota": 1,
                "DiskBackupCount": 1,
                "DeleteSnapshot": 0,
                "InstanceType": "CVM",
                "BurstPerformance": false,
                "ErrorPrompt": "Detach disk timeout, please retry later",
                "LastAttachInsId": "ins-agp4l0lx"
            }
        ]
    }
}
```

