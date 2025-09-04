**Example 1: 创建外部数据源配置**

创建外部数据源配置

Input: 

```
tccli cls CreateExternalDataSource --cli-unfold-argument  \
    --Name uuid_test \
    --Describes  \
    --Datasource 2 \
    --COSInfo.Region ap-shanghai \
    --COSInfo.Bucket test-dataflow-1254139626 \
    --COSInfo.FileAddress temp_table/uuid_test.csv \
    --COSInfo.FieldsInfo.0.FieldName appId \
    --COSInfo.FieldsInfo.0.FieldType BIGINT \
    --COSInfo.FieldsInfo.1.FieldName uuid \
    --COSInfo.FieldsInfo.1.FieldType VARCHAR \
    --TopicId a22340c8-add1-44c9-9f05-93e1bcf71a27 \
    --LogsetId 8a98c8ef-b301-4067-a98b-8cdbff172d3e
```

Output: 
```
{
    "Response": {
        "Id": "9f8127df-8b13-4552-86ae-b59a7ea007e2",
        "RequestId": "d9b0a698-f539-440c-a67a-49d7c3a2dc07"
    }
}
```

