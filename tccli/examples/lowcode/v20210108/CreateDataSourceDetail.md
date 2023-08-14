**Example 1: 创建模型**



Input: 

```
tccli lowcode CreateDataSourceDetail --cli-unfold-argument  \
    --Title abc \
    --Name abc \
    --Type abc \
    --Description abc \
    --Schema abc \
    --EnvId abc \
    --Methods abc \
    --DataSourceVersion abc \
    --SchemaVersion abc \
    --Creator abc \
    --AsyncCall 0 \
    --TemplateType 0 \
    --TemplateCode abc \
    --TicketId abc \
    --Configuration abc \
    --BindAppCode abc \
    --SubType abc \
    --CredentialInfo.SecretId abc \
    --CredentialInfo.SecretKey abc \
    --GroupId abc
```

Output: 
```
{
    "Response": {
        "Data": {
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
                    "OnlineStatusUse": 0,
                    "DataSourceId": "abc"
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
        },
        "RequestId": "abc"
    }
}
```

