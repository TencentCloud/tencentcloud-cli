**Example 1: 查询文件目录**



Input: 

```
tccli wedata ListFileSystemsPage --cli-unfold-argument  \
    --WorkspaceId 17623497097012366 \
    --FilePath /data \
    --ConnectionId 3b851dc7-bbc6-4329-b258-7f989af7381a
```

Output: 
```
{
    "Response": {
        "Data": {
            "FileSystemDetails": [
                {
                    "FileName": "clickhouse-client.tar",
                    "IsDirectory": false
                }
            ],
            "NextPageToken": "eyJsaW1pdCI6MTAsIm9mZnNldCI6MTB9"
        },
        "RequestId": "00b56d3c-3879-452e-a3a5-4295edb012c9"
    }
}
```

