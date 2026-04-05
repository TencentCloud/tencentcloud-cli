**Example 1: 获取用户所有最近24小时内上传成功但未建表的文件**



Input: 

```
tccli wedata GetRecentUploads --cli-unfold-argument  \
    --WorkspaceId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "RecentUploads": [
                {
                    "CreatedAt": "1764750162232",
                    "FileName": "basic_test.json",
                    "FilePath": "cosn://bucket-30-251436191/temp/uploads/json/basic_test.json",
                    "FileSize": "120",
                    "FileType": "json",
                    "HoursRemaining": 24
                }
            ]
        },
        "RequestId": "ef514da0-e386-40a5-a05e-328edbc666b3"
    }
}
```

