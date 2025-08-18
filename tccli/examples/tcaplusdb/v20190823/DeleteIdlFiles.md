**Example 1: 删除目标idl文件**

删除目标idl文件

Input: 

```
tccli tcaplusdb DeleteIdlFiles --cli-unfold-argument  \
    --ClusterId 6084038577 \
    --IdlFiles.0.FileName tb_example \
    --IdlFiles.0.FileType PROTO \
    --IdlFiles.0.FileExtType proto \
    --IdlFiles.0.FileSize 266 \
    --IdlFiles.0.FileId 849
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "IdlFileInfos": [
            {
                "FileName": "filename",
                "FileType": "proto",
                "FileExtType": "proto",
                "FileSize": 12230,
                "FileId": 1,
                "Error": {
                    "Code": "",
                    "Message": ""
                }
            }
        ],
        "RequestId": "16454"
    }
}
```

