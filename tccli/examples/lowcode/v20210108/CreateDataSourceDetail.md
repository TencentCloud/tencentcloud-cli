**Example 1: 创建模型**



Input: 

```
tccli lowcode CreateDataSourceDetail --cli-unfold-argument  \
    --Title  \
    --Name  \
    --Type  \
    --Description  \
    --Schema  \
    --EnvId  \
    --Methods  \
    --DataSourceVersion  \
    --SchemaVersion  \
    --Creator  \
    --AsyncCall 0 \
    --TemplateType 0 \
    --TemplateCode  \
    --TicketId  \
    --Configuration  \
    --BindAppCode  \
    --SubType  \
    --CredentialInfo.SecretId  \
    --CredentialInfo.SecretKey  \
    --GroupId 
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": "datasource",
            "Title": "datasource",
            "Name": "datasource",
            "Type": "1",
            "Description": "",
            "Schema": "",
            "CmsProject": "",
            "PkgId": "",
            "SchemaVersion": "",
            "CreatorId": "",
            "CreatedAt": "",
            "UpdatedAt": "",
            "EnvId": "",
            "DataSourceVersion": "1",
            "AppUsageList": [
                {
                    "Id": "datasource",
                    "Title": "datasource",
                    "EditStatusUse": 0,
                    "PreviewStatusUse": 0,
                    "OnlineStatusUse": 0,
                    "DataSourceId": ""
                }
            ],
            "PublishedAt": "",
            "ChildDataSourceIds": [
                ""
            ],
            "Fun": "",
            "ScfStatus": 1,
            "Methods": "",
            "ChildDataSourceNames": [
                ""
            ],
            "IsNewDataSource": 0,
            "ViewId": "",
            "Configuration": "",
            "TemplateCode": "",
            "Source": 0,
            "PublishVersion": "",
            "PublishViewId": "",
            "SubType": "",
            "AuthStatus": 0,
            "AuthInfo": {
                "AuthUser": ""
            },
            "PublishStatus": 0,
            "UpdateVersion": 0,
            "RelationFieldList": [
                {
                    "Field": "",
                    "Format": "",
                    "RelateDataSourceName": ""
                }
            ]
        },
        "RequestId": "wsxedcrfv"
    }
}
```

