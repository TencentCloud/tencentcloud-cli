**Example 1: 创建表格文件校验**

选中已上传的创建表格IDL文件并校验

Input: 

```
tccli tcaplusdb VerifyIdlFiles --cli-unfold-argument  \
    --ExistingIdlFiles.0.FileExtType proto \
    --ExistingIdlFiles.0.FileType PROTO \
    --ExistingIdlFiles.0.FileName tb_example \
    --ExistingIdlFiles.0.FileSize 0 \
    --ExistingIdlFiles.0.FileContent xx \
    --ExistingIdlFiles.0.FileId 0 \
    --TableGroupId 101 \
    --NewIdlFiles.0.FileExtType xx \
    --NewIdlFiles.0.FileType xx \
    --NewIdlFiles.0.FileName xx \
    --NewIdlFiles.0.FileSize 0 \
    --NewIdlFiles.0.FileContent xx \
    --NewIdlFiles.0.FileId 0 \
    --ClusterId 5674209986
```

Output: 
```
{
    "Response": {
        "IdlFiles": [
            {
                "FileContent": null,
                "FileExtType": "proto",
                "FileId": 564,
                "FileName": "tb_example",
                "FileSize": 261,
                "FileType": "PROTO"
            }
        ],
        "RequestId": "70707604-2031-4c7e-a85f-a52daf354eb0",
        "TableInfos": [
            {
                "Error": null,
                "IndexKeySet": "{\"Num\":0}",
                "KeyFields": "{\"KeyField\":[{\"Label\":\"required\",\"Name\":\"uin\",\"Type\":\"int64\"},{\"Crypto\":false,\"Label\":\"required\",\"Name\":\"name\",\"Type\":\"string\"}],\"Num\":2}",
                "TableGroupId": null,
                "OldKeyFields": null,
                "OldValueFields": null,
                "ShardingKeySet": "",
                "SumKeyFieldSize": 1022,
                "SumValueFieldSize": 262144,
                "TableIdlType": "PROTO",
                "TableInstanceId": null,
                "TableName": "tb_example",
                "TableType": "GENERIC",
                "TdrVersion": 1,
                "ListElementNum": null,
                "SortFieldNum": null,
                "SortRule": null,
                "ValueFields": "{\"Num\":2,\"ValueField\":[{\"Label\":\"required\",\"Name\":\"gamesvrid\",\"Type\":\"int32\"},{\"Crypto\":false,\"Label\":\"optional\",\"Name\":\"logintime\",\"Type\":\"string\"}]}"
            }
        ],
        "TotalCount": 1
    }
}
```

