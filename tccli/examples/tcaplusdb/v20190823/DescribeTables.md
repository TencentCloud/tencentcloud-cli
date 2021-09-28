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
        "RequestId": "xx",
        "TableInfos": [
            {
                "UpdatedTime": "xx",
                "ReservedVolume": 1,
                "ReservedWriteQps": 26,
                "KeyStruct": "xx",
                "ValueStruct": "xx",
                "CreatedTime": "xx",
                "Status": "xx",
                "TableGroupId": "xx",
                "TableSize": 48566336,
                "Memo": "xx",
                "ClusterId": "xx",
                "ListElementNum": 1,
                "DbClusterInfoStruct": "xx",
                "ApiAccessId": "xx",
                "TableGroupName": "xx",
                "IndexStruct": "xx",
                "ShardingKeySet": "xx",
                "ReservedReadQps": 80,
                "IdlFiles": [
                    {
                        "FileExtType": "xx",
                        "FileType": "xx",
                        "FileName": "xx",
                        "FileSize": 266,
                        "FileContent": "xx",
                        "FileId": 551
                    }
                ],
                "Error": {
                    "Message": "xx",
                    "Code": "xx"
                },
                "TableType": "xx",
                "TableIdlType": "xx",
                "ClusterName": "xx",
                "TableInstanceId": "xx",
                "SortRule": 0,
                "TableName": "xx",
                "SortFieldNum": 0
            }
        ]
    }
}
```

