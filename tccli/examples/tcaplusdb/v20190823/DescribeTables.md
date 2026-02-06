**Example 1: 查询表列表**

查询表列表

Input: 

```
tccli tcaplusdb DescribeTables --cli-unfold-argument  \
    --ClusterId 5674209986
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TableInfos": [
            {
                "TableName": "testname",
                "TableInstanceId": "tcaplus-121312",
                "TableType": "tdr",
                "TableIdlType": "tdr",
                "ClusterId": "121443121",
                "ClusterName": "clustename",
                "TableGroupId": "18433",
                "TableGroupName": "groupname",
                "KeyStruct": "keystruct",
                "ValueStruct": "valuestruct",
                "ShardingKeySet": "shardingkeyset",
                "IndexStruct": "indexstruct",
                "ListElementNum": 1024,
                "IdlFiles": [
                    {
                        "FileName": "filename",
                        "FileType": "tdr",
                        "FileExtType": "tdr",
                        "FileSize": 10240,
                        "FileId": 1,
                        "FileContent": "content"
                    }
                ],
                "ReservedVolume": 10,
                "ReservedReadQps": 1000,
                "ReservedWriteQps": 1000,
                "TableSize": 1000,
                "Status": "normal",
                "CreatedTime": "2020-10-10 10:10:10",
                "UpdatedTime": "2020-10-10 10:10:10",
                "Memo": "memo",
                "Error": {
                    "Code": "",
                    "Message": ""
                },
                "ApiAccessId": "accessid",
                "SortFieldNum": 0,
                "SortRule": 0,
                "DbClusterInfoStruct": "dbinfostruct",
                "TxhBackupExpireDay": 1,
                "SyncTableInfo": {
                    "TargetTableSplitNum": 1,
                    "TargetTableNamePrefix": [
                        "tablenameprefix"
                    ],
                    "TargetSyncDBInstanceId": "193242",
                    "TargetDatabaseName": "targetname",
                    "Status": 0,
                    "ClusterId": "193243234",
                    "TableGroupId": 1,
                    "TableName": "testname",
                    "TableId": "tcaplus-12312",
                    "KeyFieldMapping": [
                        {
                            "SourceName": "sourcename",
                            "TargetName": "targetname"
                        }
                    ],
                    "ValueFieldMapping": [
                        {
                            "SourceName": "sourcename",
                            "TargetName": "targetname"
                        }
                    ]
                }
            }
        ],
        "RequestId": "1932423-121413"
    }
}
```

