**Example 1: 列出表血缘信息**

列出表血缘信息

Input: 

```
tccli wedata DescribeColumnLineage --cli-unfold-argument  \
    --Direction BOTH \
    --Data.Id 12395550416 \
    --Data.ColumnType INT \
    --Data.ColumnName col_a1 \
    --Data.ColumnNameCn  \
    --Data.Description  \
    --Data.DatasourceId - \
    --Data.QualifiedName - \
    --Data.TableName 0210_biao1 \
    --Data.DownStreamCount 0 \
    --Data.UpStreamCount 0 \
    --Data.TableId JqDviGd3SJKP1Dzlaabbcc \
    --Data.ExtParams.0.Value 00000000-0000-0000-0000-000000000000 \
    --Data.ExtParams.0.Name nodeid \
    --Data.ExtParams.1.Value true \
    --Data.ExtParams.1.Name flag \
    --IgnoreTemp True
```

Output: 
```
{
    "Response": {
        "ColumnAggregationLineage": {
            "ChildSet": null,
            "ColumnInfoSet": [
                {
                    "ColumnName": "a",
                    "ColumnNameCn": "",
                    "ColumnType": "",
                    "CreateTime": "",
                    "DatasourceId": "",
                    "Description": "",
                    "DownStreamCount": 0,
                    "Id": null,
                    "ModifyTime": "",
                    "Params": "",
                    "PrefixPath": "",
                    "QualifiedName": null,
                    "RelationParams": "",
                    "Tasks": [],
                    "UpStreamCount": 0
                }
            ],
            "MetastoreType": null,
            "ParentId": "-",
            "ParentSet": null,
            "TableName": "0210_biao1"
        },
        "RequestId": "08e65bec-dbd8-4dde-b682-6734b5137557"
    }
}
```

