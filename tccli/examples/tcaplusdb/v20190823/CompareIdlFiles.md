**Example 1: 上传并校验修改表格结构文件**

上传并校验修改表格结构文件

Input: 

```
tccli tcaplusdb CompareIdlFiles --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --NewIdlFiles.0.FileName tb_example_modify \
    --NewIdlFiles.0.FileType PROTO \
    --NewIdlFiles.0.FileExtType proto \
    --NewIdlFiles.0.FileSize 287 \
    --NewIdlFiles.0.FileContent syntax%3d%22proto2%22%3bpackage+myTcaplusTable%3bimport+%22tcaplusservice.optionv1.proto%22%3bmessage+tb_example%7boption(tcaplusservice.tcaplus_primary_key)%3d%22uin%2cname%22%3brequired+int64+uin+%3d+1%3brequired+string+name+%3d+2%3brequired+int32+gamesvrid+%3d+3%3boptional+string+logintime+%3d+4%3boptional+int32+add_v1+%3d+5%3b%7d \
    --SelectedTables.0.TableInstanceId tcaplus-1f224454 \
    --SelectedTables.0.TableGroupId 101 \
    --SelectedTables.0.TableName tb_example \
    --SelectedTables.0.TableIdlType PROTO
```

Output: 
```
{
    "Response": {
        "IdlFiles": [
            {
                "FileName": "filename",
                "FileType": "PROTO",
                "FileExtType": "proto",
                "FileSize": 0,
                "FileId": 0,
                "FileContent": "content"
            }
        ],
        "TotalCount": 1,
        "TableInfos": [
            {
                "TableIdlType": "PROTO",
                "TableInstanceId": "tcaplus-12132",
                "TableName": "name",
                "TableType": "proto",
                "KeyFields": "keyfield",
                "OldKeyFields": "oldkey",
                "ValueFields": "value",
                "OldValueFields": "oldvalue",
                "TableGroupId": "",
                "SumKeyFieldSize": 120,
                "SumValueFieldSize": 3320,
                "IndexKeySet": "indexkeyset",
                "ShardingKeySet": "shardingkey",
                "TdrVersion": 0,
                "Error": {
                    "Code": "",
                    "Message": ""
                },
                "ListElementNum": 0,
                "SortFieldNum": 0,
                "SortRule": 0
            }
        ],
        "RequestId": "435341"
    }
}
```

