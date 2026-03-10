**Example 1: 数据集列表**



Input: 

```
tccli wedata ListApplicationDatasets --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --DashboardAccessKey 801469279624839168 \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 20
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Catalog": "c4",
                    "CreatedBy": "700002164618",
                    "CreatedOn": "1768893180863",
                    "CustomSql": "SELECT * from c4.default.lingshou",
                    "DataFrom": "SQL",
                    "DatasetVersion": 5,
                    "Description": "",
                    "DisplayName": "无标题数据集test",
                    "FieldInfoList": [
                        {
                            "CalcAggregation": "",
                            "CalcFormula": "",
                            "DataType": "DATE",
                            "DataTypePrecision": 0,
                            "DataTypeScale": 0,
                            "Description": "",
                            "DisplayName": "time",
                            "FieldCategory": "",
                            "FieldType": "PHYSICAL",
                            "FormatRule": "yyyy-MM-dd",
                            "Key": "92a3273c17690016062549d7c3752",
                            "OriginalFields": "",
                            "PhysicalFieldName": "time"
                        }
                    ],
                    "Key": "fb9e4d1f176889318086406b99645",
                    "ModifiedBy": "700002164618",
                    "ModifiedOn": "1769003451243",
                    "Owner": "700002164618",
                    "ParameterList": [],
                    "RefCount": 1,
                    "Schema": "default",
                    "TableName": "",
                    "TempCosUrl": "/801469279624839168/fb9e4d1f176889318086406b99645/DRAFT/ff8024a1716b53f2052bd1fc0c73a162_700002164618_1769001555218.csv"
                }
            ],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 20,
                "TotalCount": 5,
                "TotalPageNumber": 1
            }
        },
        "RequestId": "e170f1ca-73cd-4231-acd6-1a0397917421"
    }
}
```

