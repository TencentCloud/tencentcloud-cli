**Example 1: 上报table元数据**

上报table元数据,需要先上报database和schema(如果有)
如无schema可以填空

Input: 

```
tccli wedata ReportTable --cli-unfold-argument  \
    --DatasourceId 62112 \
    --DatabaseName default \
    --TableName luffyshi_test3 \
    --Type TABLE \
    --SchemaName default_schema \
    --Description test \
    --CreateTime 1751611555000 \
    --ModifiedTime 1751611555000 \
    --Columns.0.Name asds \
    --Columns.0.Type string \
    --Columns.0.Position 1 \
    --Columns.0.Description 2333 \
    --Columns.0.CreateTime 1751611555000 \
    --Columns.0.ModifiedTime 1751611555000
```

Output: 
```
{
    "Response": {
        "Guid": "Fuo61cKNPDivwlEwnsnUIw",
        "RequestId": "3f1b3017-113a-47a6-97f7-9097bd7667c0"
    }
}
```

