**Example 1: DescribeDataSourceList**

查询数据源列表

Input: 

```
tccli lowcode DescribeDataSourceList --cli-unfold-argument  \
    --PageSize 10 \
    --PageIndex 1 \
    --EnvId data-4jT6kVY \
    --Appids data-4jT6kVY \
    --DataSourceIds data-4jT6kVY \
    --DataSourceNames data-4jT6kVY \
    --DataSourceType data-4jT6kVY \
    --QueryOption.LikeName data-4jT6kVY \
    --QueryOption.LikeTitle data-4jT6kVY \
    --ViewIds data-4jT6kVY \
    --AppLinkStatus 0 \
    --QueryBindToApp 0 \
    --QueryConnector 0 \
    --NotQuerySubTypeList data-4jT6kVY \
    --ChannelList data-4jT6kVY \
    --QueryDataSourceRelationList True \
    --DbInstanceType data-4jT6kVY \
    --DatabaseTableNames data-4jT6kVY \
    --QuerySystemModel True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Rows": [
                {
                    "Id": "data-4jT6kVY",
                    "Title": "data-4jT6kVY",
                    "Name": "data-4jT6kVY",
                    "Type": "data-4jT6kVY",
                    "Description": "data-4jT6kVY",
                    "Schema": "data-4jT6kVY",
                    "CmsProject": "data-4jT6kVY",
                    "PkgId": "lowcode-4jT6kVY",
                    "SchemaVersion": "2.0",
                    "CreatorId": "sys_user_1",
                    "CreatedAt": "data-4jT6kVY",
                    "UpdatedAt": "data-4jT6kVY",
                    "EnvId": "lowcode-4jT6kVY",
                    "DataSourceVersion": "data-4jT6kVY",
                    "AppUsageList": [
                        {
                            "Id": "data-4jT6kVY",
                            "Title": "data-4jT6kVY",
                            "EditStatusUse": 0,
                            "PreviewStatusUse": 0,
                            "OnlineStatusUse": 0,
                            "DataSourceId": "data-4jT6kVY"
                        }
                    ],
                    "PublishedAt": "data-4jT6kVY",
                    "ChildDataSourceIds": [
                        "data-4jT6kVY"
                    ],
                    "Fun": "data-4jT6kVY",
                    "ScfStatus": 1,
                    "Methods": "data-4jT6kVY",
                    "ChildDataSourceNames": [
                        "data-4jT6kVY"
                    ],
                    "IsNewDataSource": 0,
                    "ViewId": "data-4jT6kVY",
                    "Configuration": "data-4jT6kVY",
                    "TemplateCode": "data-4jT6kVY",
                    "Source": 0,
                    "PublishVersion": "data-4jT6kVY",
                    "PublishViewId": "data-4jT6kVY",
                    "SubType": "data-4jT6kVY",
                    "AuthStatus": 0,
                    "AuthInfo": {
                        "AuthUser": "data-4jT6kVY"
                    },
                    "PublishStatus": 0,
                    "UpdateVersion": 0,
                    "RelationFieldList": [
                        {
                            "Field": "abcdata-4jT6kVY",
                            "Format": "data-4jT6kVY",
                            "RelateDataSourceName": "data-4jT6kVY"
                        }
                    ],
                    "DbInstanceType": "data-4jT6kVY",
                    "PreviewTableName": "data-4jT6kVY",
                    "PublishedTableName": "data-4jT6kVY",
                    "DbSourceType": "data-4jT6kVY"
                }
            ],
            "Count": 1
        },
        "RequestId": "1234_23232sdssasd"
    }
}
```

