**Example 1: Notebook列表**

Notebook列表

Input: 

```
tccli tione DescribeNotebooks --cli-unfold-argument  \
    --OrderField string \
    --TagFilters.0.TagValues string \
    --TagFilters.0.TagKey string \
    --Limit 0 \
    --Filters.0.Fuzzy True \
    --Filters.0.Values string \
    --Filters.0.Name string \
    --Filters.0.Negative True \
    --Offset 0 \
    --Order string
```

Output: 
```
{
    "Response": {
        "NotebookSet": [
            {
                "Id": "nb-1188508294472113920",
                "Name": "notebook-test",
                "ChargeType": "POSTPAID_BY_HOUR",
                "ResourceConf": {
                    "Gpu": 1,
                    "Cpu": 2018,
                    "GpuType": "V100",
                    "InstanceType": "TI.S.MEDIUM.POST",
                    "Memory": 4000
                },
                "ResourceGroupId": "trsg-dwpqnjmk",
                "VolumeSizeInGB": 100,
                "BillingInfos": [
                    "info"
                ],
                "Tags": [
                    {
                        "TagKey": "test-key",
                        "TagValue": "test-value"
                    }
                ],
                "CreateTime": "2024-11-11T10:50:44+08",
                "StartTime": "2024-11-11T10:51:44+08",
                "UpdateTime": "2024-11-11T10:51:44+08",
                "RuntimeInSeconds": 100,
                "ChargeStatus": "BILLING",
                "Status": "Stopped",
                "FailureReason": "errMsg",
                "EndTime": "2024-11-14T17:22:16+08",
                "PodName": "nb-1188501796310898048-912gqy8i0xvk",
                "InstanceTypeAlias": "2C4G",
                "ResourceGroupName": "resource-test",
                "AutoStopping": true,
                "AutomaticStopTime": 100,
                "VolumeSourceType": "CFS",
                "VolumeSourceCFS": {
                    "Id": "cfs-9su5kqtv",
                    "Path": "/",
                    "Protocol": "NFS",
                    "MountType": "STORAGE"
                },
                "Message": "message1",
                "UserTypes": [
                    "AiMarket"
                ],
                "SSHConfig": {
                    "Enable": true,
                    "PublicKey": "ssh-rsa AAAA*.00=",
                    "Port": 6001,
                    "LoginCommand": "ssh -p 127.0.0.1:6001"
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "ecc8d2f6-9772-40df-856f-f6e48c6a7008"
    }
}
```

