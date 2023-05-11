**Example 1: 创建云硬盘**

创建云硬盘

Input: 

```
tccli lighthouse CreateDisks --cli-unfold-argument  \
    --DiskCount 1 \
    --DiskChargePrepaid.Period 1 \
    --DiskChargePrepaid.TimeUnit m \
    --DiskName test \
    --DiskType CLOUD_PREMIUM \
    --DiskSize 20 \
    --Zone ap-hongkong-2 \
    --DiskBackupQuota 1
```

Output: 
```
{
    "Response": {
        "DiskIdSet": [
            "lhdisk-2q0cs4oe"
        ],
        "RequestId": "69765fd3-56a6-4633-8afd-72ca7805226b"
    }
}
```

