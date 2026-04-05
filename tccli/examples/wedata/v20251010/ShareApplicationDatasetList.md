**Example 1: 分享嵌出、数据集列表**



Input: 

```
tccli wedata ShareApplicationDatasetList --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --DashboardAccessKey 797848762287833088 \
    --PageRequest.AllPage True
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
                    "CreatedOn": "1768029990413",
                    "CustomSql": "SELECT * FROM `c4`.`default`.`lingshou_202601081143`",
                    "DataFrom": "SQL",
                    "DatasetVersion": 7,
                    "Description": "",
                    "DisplayName": "point",
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
                            "Key": "6b85e12ba1f64d0b17681875827439d6b24a132a64350",
                            "OriginalFields": "",
                            "PhysicalFieldName": "time"
                        }
                    ],
                    "Key": "7de5efd89b97479217680299904139f44838600d8ee0b",
                    "ModifiedBy": "700002164618",
                    "ModifiedOn": "1768187582796",
                    "Owner": "700002164618",
                    "ParameterList": [],
                    "RefCount": 3,
                    "Schema": "default",
                    "TableName": "",
                    "TempCosUrl": "open/tcbi/wedata3-chatbi-server/700002164618/pull_extra_analysis/700002164618/797848762287833088/7de5efd89b97479217680299904139f44838600d8ee0b/DRAFT/42cf259767d16d6c40b5e1079f73ac7f_700002164618_1768187485808.csv"
                }
            ],
            "PageResponse": {
                "PageNumber": 0,
                "PageSize": 0,
                "TotalCount": 1,
                "TotalPageNumber": 1
            }
        },
        "RequestId": "68b177a4-271c-4c56-af2b-4a1b01d134c7"
    }
}
```

