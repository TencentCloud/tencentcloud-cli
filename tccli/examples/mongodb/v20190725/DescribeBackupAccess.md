**Example 1: 获取实例备份下载授权**



Input: 

```
tccli mongodb DescribeBackupAccess --cli-unfold-argument  \
    --InstanceId cmgo-f0vrx2v9 \
    --BackupName cmgo-f0vrx2v9_2019-09-02_04:49
```

Output: 
```
{
    "Bucket": "cmongo-cd-backup",
    "Files": [
        {
            "File": "cmongo_hotbackup/cmgo-f0vrx2v9_0/1567370984",
            "ReplicaSetId": "cmgo-f0vrx2v9_0"
        }
    ],
    "Region": "ap-chengdu",
    "RequestId": "7e108f10-d228-11e9-b27e-9500754d2540"
}
```

