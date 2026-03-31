**Example 1: 上传文件到COS并立即预览文件内容和结构**



Input: 

```
tccli wedata UploadFilesAndPreview --cli-unfold-argument  \
    --Files.0.FilePath cosn://bucket/path/to/file1.csv \
    --Files.0.FileSize 100 \
    --Mode combine \
    --CsvDelimiter , \
    --CsvHeader True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": [
                {
                    "Fields": [
                        {
                            "Name": "id",
                            "Value": "1"
                        },
                        {
                            "Name": "name",
                            "Value": "Chinese"
                        }
                    ]
                }
            ],
            "Schema": [
                {
                    "Name": "id",
                    "Type": "bigint",
                    "Selected": true
                },
                {
                    "Name": "name",
                    "Type": "string",
                    "Selected": true
                }
            ]
        },
        "RequestId": "67f9287f-0347-4577-84f1-a05f1aeb0f6d"
    }
}
```

