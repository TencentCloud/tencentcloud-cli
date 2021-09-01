**Example 1: 删除目标idl文件**

删除目标idl文件

Input: 

```
tccli tcaplusdb DeleteIdlFiles --cli-unfold-argument  \
    --ClusterId 6084038577 \
    --IdlFiles.0.FileExtType proto \
    --IdlFiles.0.FileType PROTO \
    --IdlFiles.0.FileName tb_example \
    --IdlFiles.0.FileSize 0 \
    --IdlFiles.0.FileContent xx \
    --IdlFiles.0.FileId 0
```

Output: 
```
{
    "Response": {
        "IdlFileInfos": [
            {
                "Error": null,
                "FileExtType": "proto",
                "FileId": 849,
                "FileName": "tb_example",
                "FileSize": 266,
                "FileType": "PROTO"
            }
        ],
        "RequestId": "4e79897b-5696-4d1b-b337-d2b46824de64",
        "TotalCount": 1
    }
}
```

