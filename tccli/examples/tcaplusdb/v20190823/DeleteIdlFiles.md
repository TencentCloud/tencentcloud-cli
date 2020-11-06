**Example 1: Deleting target IDL file**

This example shows you how to delete a target IDL file.

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

