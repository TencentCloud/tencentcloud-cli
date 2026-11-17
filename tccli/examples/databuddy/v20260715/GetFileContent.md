**Example 1: demo**



Input: 

```
tccli databuddy GetFileContent --cli-unfold-argument  \
    --WorkspaceId 1**8*18***8***327 \
    --FileId 8**8*1**4****39*68
```

Output: 
```
{
    "Response": {
        "Data": {
            "Content": "MQ==",
            "ContentEncoding": "base64",
            "FileId": "89*8*1*0******9968",
            "FileName": "1.sql",
            "FilePath": "/Wor**p*ce/*ser*********0-test1@tenc************0*1***19/1.sql",
            "FileSize": "1",
            "FileType": "SQL_FILE"
        },
        "RequestId": "95d63f8f-1f17-4542-848d-76a307ead1d2"
    }
}
```

