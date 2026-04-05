**Example 1: 获取数据集详情**



Input: 

```
tccli wedata GetApplicationDataset --cli-unfold-argument  \
    --Key a666ca9f1769004244669034c2c98 \
    --WorkspaceId 17663856806379896 \
    --DashboardAccessKey 801934639037759488
```

Output: 
```
{
    "Response": {
        "Data": {
            "Catalog": "",
            "CreatedBy": "700002164618",
            "CreatedOn": "1769004244669",
            "CustomSql": "",
            "DataFrom": "SQL",
            "DatasetVersion": 0,
            "DatasourceType": "",
            "Description": "",
            "DisplayName": "无标题数据集1",
            "FieldInfoList": [],
            "Key": "a666ca9f1769004244669034c2c98",
            "ModelType": "",
            "ModifiedBy": "700002164618",
            "ModifiedOn": "1769004244669",
            "Objects": "",
            "Owner": "700002164618",
            "ParameterList": [],
            "Schema": "",
            "TableName": "",
            "TempCosUrl": ""
        },
        "RequestId": "d6feff2f-9994-4d8d-9f82-a69b6428978c"
    }
}
```

