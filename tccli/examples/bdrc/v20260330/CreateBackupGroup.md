**Example 1: 创建备份组**



Input: 

```
tccli bdrc CreateBackupGroup --cli-unfold-argument  \
    --DiskIds disk-22u8462w \
    --BackupGroupName kairoslliu_test_bakcupgroup
```

Output: 
```
{
    "Response": {
        "BackupGroupId": "cbackup-n3thksnh",
        "RequestId": "a2dd25d8-3f06-4622-be4c-44315fc9d5e5"
    }
}
```

