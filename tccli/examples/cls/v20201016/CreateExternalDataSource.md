**Example 1: 创建外部数据源配置**

创建外部数据源配置

Input: 

```
tccli cls CreateExternalDataSource --cli-unfold-argument  \
    --Name abc \
    --Describes abc \
    --Datasource 1 \
    --SQLInfo.AccessMode 1 \
    --SQLInfo.Address abc \
    --SQLInfo.Port abc \
    --SQLInfo.EndPointServiceId abc \
    --SQLInfo.User abc \
    --SQLInfo.Password abc \
    --SQLInfo.DatabaseName abc \
    --SQLInfo.TableName abc \
    --COSInfo.Region abc \
    --COSInfo.Bucket abc \
    --COSInfo.FileAddress abc \
    --COSInfo.FieldsInfo.0.FieldName abc \
    --COSInfo.FieldsInfo.0.FieldType abc \
    --TopicId abc \
    --LogsetId abc
```

Output: 
```
{
    "Response": {
        "Id": "abc",
        "RequestId": "abc"
    }
}
```

