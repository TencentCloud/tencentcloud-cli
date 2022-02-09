**Example 1: 获取数据源详情列表**



Input: 

```
tccli lowcode DescribeDataSourceList --cli-unfold-argument  \
    --PageIndex 0 \
    --PageSize 0 \
    --EnvId aaa
```

Output: 
```
{
    "Response": {
        "Data": {
            "Count": 0,
            "Rows": [
                {
                    "IsNewDataSource": 0,
                    "ChildDataSourceNames": [
                        "xx"
                    ],
                    "CmsProject": "xx",
                    "CreatorId": "xx",
                    "AuthStatus": 0,
                    "Type": "xx",
                    "AppUsageList": [
                        {
                            "OnlineStatusUse": 0,
                            "PreviewStatusUse": 0,
                            "Id": "xx",
                            "EditStatusUse": 0,
                            "Title": "xx"
                        }
                    ],
                    "Schema": "xx",
                    "PkgId": "xx",
                    "Description": "xx",
                    "ScfStatus": 1,
                    "PublishVersion": "xx",
                    "ViewId": "xx",
                    "Title": "xx",
                    "PublishedAt": "xx",
                    "TemplateCode": "xx",
                    "DataSourceVersion": "xx",
                    "UpdatedAt": "xx",
                    "Configuration": "xx",
                    "CreatedAt": "xx",
                    "EnvId": "xx",
                    "Name": "xx",
                    "ChildDataSourceIds": [
                        "xx"
                    ],
                    "Fun": "xx",
                    "Methods": "xx",
                    "SubType": "database",
                    "Source": 0,
                    "SchemaVersion": "xx",
                    "PublishViewId": "xx",
                    "Id": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

