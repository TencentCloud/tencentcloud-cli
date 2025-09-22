**Example 1: 查询资源文件列表**



Input: 

```
tccli wedata ListResourceFiles --cli-unfold-argument  \
    --ProjectId 146094787xxxx7296 \
    --PageNumber 1 \
    --PageSize 10 \
    --ResourceName wedata_a \
    --ParentFolderPath /qmxxxxu \
    --CreateUserUin 10002xxx06 \
    --ModifyTimeStart 2025-08-25 22:00:00 \
    --ModifyTimeEnd 2025-08-26 23:00:00 \
    --CreateTimeStart 2025-08-25 22:00:00 \
    --CreateTimeEnd 2025-08-26 23:00:00
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "FileExtensionType": "",
                    "ResourceId": "3b119eee-8c78-4921-b8d6-acce32dfcd19",
                    "ResourceName": "wedata_a"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPageNumber": 1
        },
        "RequestId": "f0beb4e0-7035-4353-a8b0-f0099cd6cf47"
    }
}
```

