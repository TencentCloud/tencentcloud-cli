**Example 1: create table**

创建表

Input: 

```
tccli tccatalog CreateTable --cli-unfold-argument  \
    --CatalogName yyyy \
    --SchemaName kkkk \
    --TableName mmmm \
    --TableFormat v1 \
    --Comment asas \
    --Columns.0.Name id \
    --Columns.0.Type int \
    --Columns.0.Comment id字段 \
    --Partitioning.0.Strategy Bucket \
    --Partitioning.0.NumBuckets 3 \
    --Partitioning.0.FieldName id \
    --Properties.0.Key  \
    --Properties.0.Value  \
    --Indexes.0.Type primary_key \
    --Indexes.0.Name pk_id \
    --Indexes.0.FieldNames title description
```

Output: 
```
{
    "Response": {
        "RequestId": "e634125c-b612-471a-90a2-d85a4e368ab2"
    }
}
```

