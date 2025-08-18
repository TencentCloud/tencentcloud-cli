**Example 1: 创建表格文件校验**

选中已上传的创建表格IDL文件并校验

Input: 

```
tccli tcaplusdb VerifyIdlFiles --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --TableGroupId 101 \
    --ExistingIdlFiles.0.FileName tb_example \
    --ExistingIdlFiles.0.FileSize 261 \
    --ExistingIdlFiles.0.FileExtType proto \
    --ExistingIdlFiles.0.FileId 551 \
    --ExistingIdlFiles.0.FileType PROTO
```

Output: 
```
{
    "Response": {
        "IdlFiles": [
            {
                "FileContent": "content",
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
                "IndexKeySet": "{\"Num\":0}",
                "KeyFields": "{\"KeyField\":[{\"Label\":\"required\",\"Name\":\"uin\",\"Type\":\"int64\"},{\"Crypto\":false,\"Label\":\"required\",\"Name\":\"name\",\"Type\":\"string\"}],\"Num\":2}",
                "TableGroupId": "212412",
                "OldKeyFields": "",
                "OldValueFields": "",
                "ShardingKeySet": "",
                "SumKeyFieldSize": 1022,
                "SumValueFieldSize": 262144,
                "TableIdlType": "PROTO",
                "TableInstanceId": "",
                "TableName": "tb_example",
                "TableType": "GENERIC",
                "TdrVersion": 1,
                "ListElementNum": 1024,
                "SortFieldNum": 1,
                "SortRule": 1,
                "ValueFields": "{\"Num\":2,\"ValueField\":[{\"Label\":\"required\",\"Name\":\"gamesvrid\",\"Type\":\"int32\"},{\"Crypto\":false,\"Label\":\"optional\",\"Name\":\"logintime\",\"Type\":\"string\"}]}"
            }
        ],
        "TotalCount": 1
    }
}
```

