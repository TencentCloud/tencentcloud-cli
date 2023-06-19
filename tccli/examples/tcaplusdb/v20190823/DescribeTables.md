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
                "TableName": "abc",
                "TableInstanceId": "abc",
                "TableType": "abc",
                "TableIdlType": "abc",
                "ClusterId": "abc",
                "ClusterName": "abc",
                "TableGroupId": "abc",
                "TableGroupName": "abc",
                "KeyStruct": "abc",
                "ValueStruct": "abc",
                "ShardingKeySet": "abc",
                "IndexStruct": "abc",
                "ListElementNum": 1,
                "IdlFiles": [
                    {
                        "FileName": "abc",
                        "FileType": "abc",
                        "FileExtType": "abc",
                        "FileSize": 0,
                        "FileId": 0,
                        "FileContent": "abc"
                    }
                ],
                "ReservedVolume": 0,
                "ReservedReadQps": 0,
                "ReservedWriteQps": 0,
                "TableSize": 0,
                "Status": "abc",
                "CreatedTime": "abc",
                "UpdatedTime": "abc",
                "Memo": "abc",
                "Error": {
                    "Code": "abc",
                    "Message": "abc"
                },
                "ApiAccessId": "abc",
                "SortFieldNum": 0,
                "SortRule": 0,
                "DbClusterInfoStruct": "abc",
                "TxhBackupExpireDay": 1,
                "SyncTableInfo": {
                    "TargetTableSplitNum": 1,
                    "TargetTableNamePrefix": [
                        "abc"
                    ],
                    "TargetSyncDBInstanceId": "abc",
                    "TargetDatabaseName": "abc",
                    "Status": 0,
                    "ClusterId": "abc",
                    "TableGroupId": 1,
                    "TableName": "abc",
                    "TableId": "abc",
                    "KeyFieldMapping": [
                        {
                            "SourceName": "abc",
                            "TargetName": "abc"
                        }
                    ],
                    "ValueFieldMapping": [
                        {
                            "SourceName": "abc",
                            "TargetName": "abc"
                        }
                    ]
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

