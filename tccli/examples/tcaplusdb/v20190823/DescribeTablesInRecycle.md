**Example 1: 查询回收站表格列表**

查询回收站表格列表

Input: 

```
tccli tcaplusdb DescribeTablesInRecycle --cli-unfold-argument  \
    --TableGroupIds xx \
    --ClusterId 5674209986 \
    --Limit 0 \
    --Filters.0.Name xx \
    --Filters.0.Value xx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "5d7da70a-2aa6-4e61-9389-46a92770974c",
        "TableInfos": [
            {
                "ApiAccessId": "10",
                "ClusterName": "gz测试App",
                "ClusterId": "5674209986",
                "CreatedTime": "2019-08-29 22:03:27",
                "Error": null,
                "IdlFiles": [
                    {
                        "FileContent": null,
                        "FileExtType": "proto",
                        "FileId": 551,
                        "FileName": "tb_example",
                        "FileSize": 266,
                        "FileType": "PROTO"
                    }
                ],
                "IndexStruct": null,
                "KeyStruct": null,
                "ListElementNum": 1,
                "TableGroupId": "101",
                "Memo": null,
                "ReservedReadQps": 80,
                "ReservedVolume": 1,
                "ReservedWriteQps": 26,
                "ShardingKeySet": "key",
                "Status": "RECYCLING",
                "TableIdlType": "PROTO",
                "TableInstanceId": "tcaplus-1f224454",
                "TableName": "tb_example",
                "TableSize": 48566336,
                "TableType": "GENERIC",
                "UpdatedTime": "",
                "ValueStruct": null,
                "SortFieldNum": null,
                "SortRule": null,
                "TableGroupName": "test_zone_1"
            }
        ],
        "TotalCount": 1
    }
}
```

