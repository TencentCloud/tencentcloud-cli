**Example 1: 修改备份过期时间**



Input: 

```
tccli mongodb ModifyBackupExpireTime --cli-unfold-argument  \
    --InstanceId cmgo-******** \
    --ExpireTime 2026-06-06 04:02:00 \
    --BackupIds 11123430
```

Output: 
```
{
    "Response": {
        "FailedBackups": [
            21123430
        ],
        "RequestId": "35a28e4e-a5bf-441a-8729-b63442bd5cf2"
    }
}
```

