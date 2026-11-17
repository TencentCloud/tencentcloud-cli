**Example 1: 查询全量备份集详情**



Input: 

```
tccli dbs DescribeFullBackupSetDetail --cli-unfold-argument  \
    --BackupSetId backupset-qvmga518
```

Output: 
```
{
    "Response": {
        "BackupSet": {
            "BackupMethod": "logical",
            "BackupObject": {
                "ObjectItems": [],
                "ObjectMode": "all"
            },
            "BackupPool": "DefaultPool",
            "BackupSetId": "backupset-qvmga518",
            "BackupSetOption": {
                "Encryption": "UnEncrypted"
            },
            "BackupSize": 991853615,
            "EndTime": "2026-04-28 01:03:35",
            "ErrorMessage": {
                "Message": "",
                "Title": ""
            },
            "ExpireTime": "2026-05-01 01:03:35",
            "Progress": {
                "DataProgress": 100,
                "SchemaProgress": 100
            },
            "ResourceDetail": {
                "StayTime": 0,
                "TieredType": "standard"
            },
            "RetentionType": "standard",
            "SourceEndpoint": {
                "AccessType": "cdb",
                "CcnId": "",
                "CvmInstanceId": "",
                "DBKernel": "",
                "DatabaseType": "mysql",
                "EngineVersion": "8.0",
                "InstanceId": "cdb-ai2oxphl",
                "Ip": "",
                "Password": "",
                "Port": 0,
                "Region": "ap-guangzhou",
                "Role": "",
                "SubnetId": "",
                "Supplier": "others",
                "UniqDcgId": "",
                "UniqVpnGwId": "",
                "UserName": "root",
                "VpcId": ""
            },
            "SourceInfo": "cdb-ai2oxphl",
            "StartTime": "2026-04-28 01:02:04",
            "Status": "finished",
            "StorageType": "DBSStorage"
        },
        "RequestId": "fc1b4708-1ccf-49b5-adf9-feb2acea998a"
    }
}
```

