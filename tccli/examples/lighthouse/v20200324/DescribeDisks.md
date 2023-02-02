**Example 1: 查询磁盘**

查询磁盘

Input: 

```
tccli lighthouse DescribeDisks --cli-unfold-argument  \
    --DiskIds lhdisk-p1zflrif
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DiskSet": [
            {
                "DiskId": "lhdisk-p1zflrif",
                "InstanceId": "lhins-anxwfvxh",
                "Zone": "ap-guangzhou-3",
                "DiskName": "lhdisk-p1zflrif-system-disk",
                "DiskUsage": "DATA_DISK",
                "DiskType": "CLOUD_PREMIUM",
                "DiskChargeType": "PREPAID",
                "DiskSize": 30,
                "RenewFlag": "NOTIFY_AND_AUTO_RENEW",
                "DiskState": "ATTACHED",
                "Attached": true,
                "DeleteWithInstance": false,
                "DiskBackupCount": 1,
                "DiskBackupQuota": 1,
                "LatestOperation": "DetachDisks",
                "LatestOperationState": "FAILED",
                "LatestOperationRequestId": "54118bb6-7206-43f7-bf53-b77a394ad51e",
                "CreatedTime": "2021-08-25T08:50:57Z",
                "ExpiredTime": "2021-10-28T09:11:37Z",
                "IsolatedTime": null
            }
        ],
        "RequestId": "b362f486-571c-4094-afd5-22a38bd63046"
    }
}
```

