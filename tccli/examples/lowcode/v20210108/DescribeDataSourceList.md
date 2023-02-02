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
            "Count": 1,
            "Rows": [
                {
                    "AppUsageList": [
                        {
                            "EditStatusUse": 0,
                            "Id": "",
                            "OnlineStatusUse": 0,
                            "PreviewStatusUse": 0,
                            "Title": ""
                        }
                    ],
                    "AuthInfo": {
                        "AuthUser": ""
                    },
                    "AuthStatus": 0,
                    "ChildDataSourceIds": [
                        ""
                    ],
                    "ChildDataSourceNames": [
                        ""
                    ],
                    "CmsProject": "0",
                    "Configuration": "",
                    "CreatedAt": "",
                    "CreatorId": "",
                    "DataSourceVersion": "",
                    "Description": "",
                    "EnvId": "",
                    "Fun": "",
                    "Id": "",
                    "IsNewDataSource": 0,
                    "Methods": "",
                    "Name": "",
                    "PkgId": "",
                    "PublishStatus": 0,
                    "PublishVersion": "",
                    "PublishViewId": "",
                    "PublishedAt": "",
                    "ScfStatus": 0,
                    "Schema": "",
                    "SchemaVersion": "",
                    "Source": 0,
                    "SubType": "",
                    "TemplateCode": "",
                    "Title": "",
                    "Type": "",
                    "UpdateVersion": 0,
                    "UpdatedAt": "",
                    "ViewId": ""
                }
            ]
        },
        "RequestId": "374c93bd-253a-41e7-afc2-922af046beac"
    }
}
```

