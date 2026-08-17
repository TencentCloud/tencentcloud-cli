**Example 1: 查询备份组的操作掩码**



Input: 

```
tccli bdrc DescribeBackupGroupsDeniedActions --cli-unfold-argument  \
    --BackupGroupIds cbackup-n3thksnh
```

Output: 
```
{
    "Response": {
        "BackupGroupDeniedActionSet": [
            {
                "BackupGroupId": "cbackup-n3thksnh",
                "DeniedActions": [
                    {
                        "Action": "CreateDisks",
                        "Code": "UnsupportedOperation.NotSupported",
                        "Message": "备份组包含系统盘备份，不支持新建云硬盘"
                    }
                ]
            }
        ],
        "RequestId": "50a49442-ec5e-4771-a976-6e36839473ee"
    }
}
```

