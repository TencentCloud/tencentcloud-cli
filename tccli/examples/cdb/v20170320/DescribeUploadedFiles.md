**Example 1: 查询导入SQL文件列表**



Input: 

```
tccli cdb DescribeUploadedFiles --cli-unfold-argument  \
    --Path 100000983328
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 1,
        "Items": [
            {
                "UploadTime": "2016-11-28 15:16:13",
                "UploadInfo": {
                    "AllSliceNum": 5,
                    "CompleteNum": 3
                },
                "FileName": "joellwang.sql",
                "FileSize": 8581633,
                "IsUploadFinished": 0,
                "FileId": "5596d7433fe211da4b487228db4e7c57"
            }
        ]
    }
}
```

