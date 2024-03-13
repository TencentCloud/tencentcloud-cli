**Example 1: 获取内置镜像列表**



Input: 

```
tccli tione DescribeBuildInImages --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "RequestId",
        "BuildInImageInfos": [
            {
                "ImageName": "Name1",
                "ImageType": "SYSTEM",
                "ImageUrl": "ImageUrl1",
                "RegistryRegion": "",
                "RegistryId": "",
                "AllowSaveAllContent": false
            },
            {
                "ImageName": "Name2",
                "ImageType": "SYSTEM",
                "ImageUrl": "ImageUrl2",
                "RegistryRegion": "",
                "RegistryId": "",
                "AllowSaveAllContent": true
            }
        ]
    }
}
```

