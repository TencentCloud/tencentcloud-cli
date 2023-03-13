**Example 1: 查询数据备份文件列表**

查询数据备份文件列表

Input: 

```
tccli cdb DescribeBackups --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 2,
        "Items": [
            {
                "Status": "SUCCESS",
                "FinishTime": "2017-07-23 12:03:42",
                "Name": "ivansqwutestdr_backup_20170429000134",
                "IntranetUrl": "http://gz.tencent.com",
                "Creator": "SYSTEM",
                "BackupId": 12445233,
                "Date": "2017-04-29 00:01:34",
                "StartTime": "2017-07-22 00:01:34",
                "InternetUrl": "http://gz.tencent.com",
                "Type": "logical",
                "Way": "automatic",
                "ManualBackupName": "ab",
                "SaveMode": "save_mode_regular",
                "RemoteInfo": [],
                "Region": "ap-guangzhou",
                "Method": "full",
                "CosStorageType": 0,
                "Size": 653226,
                "InstanceId": "cdb-sadq",
                "EncryptionFlag": "off"
            },
            {
                "Status": "SUCCESS",
                "FinishTime": "2017-07-23 12:03:42",
                "StartTime": "2017-07-23 00:01:34",
                "Name": "ivansqwutestdr_backup_20170430000129",
                "IntranetUrl": "http://gz.tencent.com",
                "Creator": "SYSTEM",
                "BackupId": 436184134,
                "Date": "2017-04-30 00:01:29",
                "InternetUrl": "http://gz.tencent.com",
                "Type": "logical",
                "Way": "automatic",
                "ManualBackupName": "abv",
                "SaveMode": "save_mode_regular",
                "RemoteInfo": [],
                "Region": "ap-guangzhou",
                "Method": "full",
                "CosStorageType": 0,
                "Size": 653226,
                "InstanceId": "cdb-asdqwdqd",
                "EncryptionFlag": "on"
            }
        ]
    }
}
```

