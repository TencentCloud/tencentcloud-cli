**Example 1: 示例1**

示例1

Input: 

```
tccli wedata GetLogicTable --cli-unfold-argument  \
    --RuleId ruleId \
    --DatasourceType MYSQL \
    --DataStructs.0.DatasourceId 78b55a1d2b61 \
    --DataStructs.0.DatabaseStructs.0.DatabaseName dbA \
    --DataStructs.0.DatabaseStructs.0.SchemaStructs.0.SchemaName schemaA \
    --DataStructs.0.DatabaseStructs.0.SchemaStructs.0.Tables tableA \
    --DataStructs.0.DatabaseStructs.0.Tables tableA \
    --DataStructs.0.Instance instanceA \
    --WorkspaceId 12399sd79231 \
    --TaskId ta-ssaadf
```

Output: 
```
{
    "Response": {
        "Data": {
            "LogicColumnInfos": [
                {
                    "ColumnKey": "columnkeyA",
                    "ColumnName": "columnA",
                    "ColumnType": "string",
                    "Description": "descriptionA",
                    "TableName": "tableABC"
                }
            ]
        },
        "RequestId": "a693b6fe-a841-435e-b911-482d250202bd"
    }
}
```

