**Example 1: 查询浏览记录**

查询浏览记录

Input: 

```
tccli wedata ListAssetViews --cli-unfold-argument  \
    --Keyword t1
```

Output: 
```
{
    "Response": {
        "RequestId": "d347bb7a-ce17-4b8d-910c-99ca6a9b8480",
        "Data": {
            "TotalCount": "10",
            "Items": [
                {
                    "AssetName": "t1",
                    "AssetType": "TABLE",
                    "Comment": "",
                    "CreateTime": "2025-10-29T14:17:53+08:00",
                    "FullName": "c.s.t1"
                }
            ]
        }
    }
}
```

**Example 2: 查询资产浏览记录**

查询资产浏览记录

Input: 

```
tccli wedata ListAssetViews --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": "10",
            "Items": [
                {
                    "AssetName": "md5",
                    "AssetType": "MODEL",
                    "Comment": "",
                    "CreateTime": "2025-10-29T15:23:54+08:00",
                    "FullName": "c.s.md5"
                }
            ]
        },
        "RequestId": "16fd2880-b456-4802-a241-f959a2aeffa1"
    }
}
```

