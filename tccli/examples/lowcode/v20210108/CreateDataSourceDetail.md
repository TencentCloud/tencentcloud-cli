**Example 1: 创建数据源详情**



Input: 

```
tccli lowcode CreateDataSourceDetail --cli-unfold-argument  \
    --EnvId xx \
    --Name xx \
    --Title xx \
    --Creator xx \
    --Methods xx \
    --DataSourceVersion xx \
    --SchemaVersion xx \
    --Schema xx \
    --Type xx \
    --Description xx
```

Output: 
```
{
    "Response": {
        "Data": {
            "PkgId": "xx",
            "EnvId": "xx",
            "Name": "xx",
            "Title": "xx",
            "ScfStatus": 1,
            "PublishedAt": "xx",
            "Fun": "xx",
            "DataSourceVersion": "xx",
            "AppUsageList": [
                {
                    "OnlineStatusUse": 0,
                    "PreviewStatusUse": 0,
                    "Id": "xx",
                    "EditStatusUse": 0,
                    "Title": "xx"
                }
            ],
            "CreatorId": "xx",
            "ChildDataSourceIds": [
                "xx"
            ],
            "CmsProject": "xx",
            "UpdatedAt": "xx",
            "SchemaVersion": "xx",
            "Schema": "xx",
            "Type": "xx",
            "Id": "xx",
            "CreatedAt": "xx",
            "Description": "xx"
        },
        "RequestId": "xx"
    }
}
```

