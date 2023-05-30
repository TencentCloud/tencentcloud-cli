**Example 1: example**

查询数据源列表

Input: 

```
tccli lowcode DescribeDataSourceList --cli-unfold-argument  \
    --PageIndex 1 \
    --EnvId 字符串 \
    --QueryOption.LikeTitle 字符串 \
    --QueryOption.LikeName 字符串 \
    --PageSize 1 \
    --DataSourceType 字符串 \
    --NotQuerySubTypeList 字符串 \
    --DataSourceNames 字符串 \
    --ViewIds 字符串 \
    --QueryBindToApp 1 \
    --QueryConnector 1 \
    --DataSourceIds 字符串 \
    --Appids 字符串 \
    --ChannelList 字符串 \
    --AppLinkStatus 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Rows": [
                {
                    "Id": "abc",
                    "Title": "abc",
                    "Name": "abc",
                    "Type": "abc",
                    "Description": "abc",
                    "Schema": "abc",
                    "CmsProject": "abc",
                    "PkgId": "abc",
                    "SchemaVersion": "abc",
                    "CreatorId": "abc",
                    "CreatedAt": "abc",
                    "UpdatedAt": "abc",
                    "EnvId": "abc",
                    "DataSourceVersion": "abc",
                    "AppUsageList": [
                        {
                            "Id": "abc",
                            "Title": "abc",
                            "EditStatusUse": 0,
                            "PreviewStatusUse": 0,
                            "OnlineStatusUse": 0
                        }
                    ],
                    "PublishedAt": "abc",
                    "ChildDataSourceIds": [
                        "abc"
                    ],
                    "Fun": "abc",
                    "ScfStatus": 1,
                    "Methods": "abc",
                    "ChildDataSourceNames": [
                        "abc"
                    ],
                    "IsNewDataSource": 0,
                    "ViewId": "abc",
                    "Configuration": "abc",
                    "TemplateCode": "abc",
                    "Source": 0,
                    "PublishVersion": "abc",
                    "PublishViewId": "abc",
                    "SubType": "abc",
                    "AuthStatus": 0,
                    "AuthInfo": {
                        "AuthUser": "abc"
                    },
                    "PublishStatus": 0,
                    "UpdateVersion": 0,
                    "RelationFieldList": [
                        {
                            "Field": "abc",
                            "Format": "abc",
                            "RelateDataSourceName": "abc"
                        }
                    ]
                }
            ],
            "Count": 0
        },
        "RequestId": "abc"
    }
}
```

