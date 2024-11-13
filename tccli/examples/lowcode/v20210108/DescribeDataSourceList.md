**Example 1: example**

查询数据源列表

Input: 

```
tccli lowcode DescribeDataSourceList --cli-unfold-argument  \
    --PageSize 0 \
    --PageIndex 0 \
    --EnvId abc \
    --Appids abc \
    --DataSourceIds abc \
    --DataSourceNames abc \
    --DataSourceType abc \
    --QueryOption.LikeName abc \
    --QueryOption.LikeTitle abc \
    --ViewIds abc \
    --AppLinkStatus 0 \
    --QueryBindToApp 0 \
    --QueryConnector 0 \
    --NotQuerySubTypeList abc \
    --ChannelList abc \
    --QueryDataSourceRelationList True \
    --DbInstanceType abc \
    --DatabaseTableNames abc \
    --QuerySystemModel True
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
                    "DbSourceType": "abc",
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

