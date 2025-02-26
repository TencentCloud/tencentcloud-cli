**Example 1: DescribeDataSourceList**

查询数据源列表

Input: 

```
tccli lowcode DescribeDataSourceList --cli-unfold-argument  \
    --PageSize 10 \
    --PageIndex 1 \
    --EnvId lowcode-4jT6kVY \
    --Appids data-4jT6kVY \
    --DataSourceIds data-4jT6kVY \
    --DataSourceNames 4jT6kVY \
    --DataSourceType mysql \
    --QueryOption.LikeName 4jT6kVY \
    --QueryOption.LikeTitle 用户 \
    --ViewIds 4jT6kVY \
    --AppLinkStatus 0 \
    --QueryBindToApp 0 \
    --QueryConnector 0 \
    --NotQuerySubTypeList d4jT6kVY \
    --ChannelList 4jT6kVY \
    --QueryDataSourceRelationList True \
    --DbInstanceType mysql \
    --DatabaseTableNames sys_user \
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
                    "Title": "用户",
                    "Name": "sys_user",
                    "Type": "database",
                    "Description": "内置数据源",
                    "Schema": "{\"x-primary-column\":\"name\",\"x-kind\":\"tcb\",\"name\":\"sys_user\",\"x-defaultMethods\":[\"wedaCreate\"]}",
                    "CmsProject": "data-4jT6kVY",
                    "PkgId": "lowcode-4jT6kVY",
                    "SchemaVersion": "2.0",
                    "CreatorId": "sys_user_1",
                    "CreatedAt": "sys",
                    "UpdatedAt": "sys",
                    "EnvId": "lowcode-4jT6kVY",
                    "DataSourceVersion": "data-4jT6kVY",
                    "AppUsageList": [
                        {
                            "Id": "data-4jT6kVY",
                            "Title": "用户",
                            "EditStatusUse": 0,
                            "PreviewStatusUse": 0,
                            "OnlineStatusUse": 0,
                            "DataSourceId": "data-4jT6kVY"
                        }
                    ],
                    "PublishedAt": "sys",
                    "ChildDataSourceIds": [
                        "data-4jT6kVY"
                    ],
                    "Fun": "{\"prviewPublishAt\":\"2024-11-19T17:28:57.919+0800\",\"onlinePublishAt\":\"2024-11-19T17:28:30.989+0800\",\"previewVersion\":2,\"onlineVersion\":2}",
                    "ScfStatus": 1,
                    "Methods": "data-4jT6kVY",
                    "ChildDataSourceNames": [
                        "data-4jT6kVY"
                    ],
                    "IsNewDataSource": 0,
                    "ViewId": "view-67vvgoe840",
                    "Configuration": "data-4jT6kVY",
                    "TemplateCode": "data-4jT6kVY",
                    "Source": 0,
                    "PublishVersion": "data-4jT6kVY",
                    "PublishViewId": "data-4jT6kVY",
                    "SubType": "data-4jT6kVY",
                    "AuthStatus": 0,
                    "AuthInfo": {
                        "AuthUser": "sys"
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
                    "DbInstanceType": "mysql",
                    "PreviewTableName": "sys_user_pre",
                    "PublishedTableName": "sys_user",
                    "DbSourceType": "mysql"
                }
            ],
            "Count": 1
        },
        "RequestId": "1234_23232sdssasd"
    }
}
```

