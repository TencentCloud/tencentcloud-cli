**Example 1: 上传并校验修改表格结构文件**

上传并校验修改表格结构文件

Input: 

```
tccli tcaplusdb CompareIdlFiles --cli-unfold-argument  \
    --ExistingIdlFiles.0.FileExtType xx \
    --ExistingIdlFiles.0.FileType xx \
    --ExistingIdlFiles.0.FileName xx \
    --ExistingIdlFiles.0.FileSize 0 \
    --ExistingIdlFiles.0.FileContent xx \
    --ExistingIdlFiles.0.FileId 0 \
    --NewIdlFiles.0.FileExtType proto \
    --NewIdlFiles.0.FileType PROTO \
    --NewIdlFiles.0.FileName tb_example_modify \
    --NewIdlFiles.0.FileSize 0 \
    --NewIdlFiles.0.FileContent syntax%3d%22proto2%22%3bpackage+myTcaplusTable%3bimport+%22tcaplusservice.optionv1.proto%22%3bmessage+tb_example%7boption(tcaplusservice.tcaplus_primary_key)%3d%22uin%2cname%22%3brequired+int64+uin+%3d+1%3brequired+string+name+%3d+2%3brequired+int32+gamesvrid+%3d+3%3boptional+string+logintime+%3d+4%3boptional+int32+add_v1+%3d+5%3b%7d \
    --NewIdlFiles.0.FileId 0 \
    --ClusterId 5674209986 \
    --SelectedTables.0.TableIdlType PROTO \
    --SelectedTables.0.TableGroupId 101 \
    --SelectedTables.0.FileExtType xx \
    --SelectedTables.0.TableInstanceId tcaplus-1f224454 \
    --SelectedTables.0.Memo xx \
    --SelectedTables.0.TableName tb_example \
    --SelectedTables.0.ReservedReadQps 0 \
    --SelectedTables.0.ListElementNum 0 \
    --SelectedTables.0.ReservedVolume 0 \
    --SelectedTables.0.ReservedWriteQps 0 \
    --SelectedTables.0.FileSize 0 \
    --SelectedTables.0.FileContent xx \
    --SelectedTables.0.FileName xx \
    --SelectedTables.0.TableType xx
```

Output: 
```
{
    "Response": {
        "IdlFiles": [
            {
                "FileContent": null,
                "FileExtType": "proto",
                "FileId": 600,
                "FileName": "tb_example_modify",
                "FileSize": 287,
                "FileType": "PROTO"
            }
        ],
        "RequestId": "81274902-0df6-4574-a3b0-2ea229ef903f",
        "TableInfos": [
            {
                "Error": null,
                "IndexKeySet": null,
                "KeyFields": "{\"KeyField\":[{\"Label\":\"required\",\"Name\":\"uin\",\"Type\":\"int64\"},{\"Crypto\":false,\"Label\":\"required\",\"Name\":\"name\",\"Type\":\"string\"}],\"Num\":2}",
                "TableGroupId": "101",
                "OldKeyFields": "{\"KeyField\":[{\"Label\":\"required\",\"Name\":\"uin\",\"Type\":\"int64\"},{\"Crypto\":false,\"Label\":\"required\",\"Name\":\"name\",\"Type\":\"string\"}],\"Num\":2}",
                "OldValueFields": "{\"Num\":2,\"ValueField\":[{\"Label\":\"required\",\"Name\":\"gamesvrid\",\"Type\":\"int32\"},{\"Crypto\":false,\"Label\":\"optional\",\"Name\":\"logintime\",\"Type\":\"string\"}]}",
                "ShardingKeySet": "",
                "SumKeyFieldSize": 1022,
                "SumValueFieldSize": 262144,
                "TableIdlType": "PROTO",
                "TableInstanceId": "tcaplus-1f224454",
                "TableName": "tb_example",
                "TableType": "GENERIC",
                "TdrVersion": 1,
                "ListElementNum": null,
                "SortFieldNum": null,
                "SortRule": null,
                "ValueFields": "{\"Num\":3,\"ValueField\":[{\"Label\":\"required\",\"Name\":\"gamesvrid\",\"Type\":\"int32\"},{\"Crypto\":false,\"Label\":\"optional\",\"Name\":\"logintime\",\"Type\":\"string\"},{\"Label\":\"optional\",\"Name\":\"add_v1\",\"Type\":\"int32\"}]}"
            }
        ],
        "TotalCount": 1
    }
}
```

