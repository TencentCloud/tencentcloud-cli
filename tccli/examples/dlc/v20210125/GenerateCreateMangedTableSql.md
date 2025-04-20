**Example 1: 创建托管存储内表**

创建托管存储内表

Input: 

```
tccli dlc GenerateCreateMangedTableSql --cli-unfold-argument  \
    --TableBaseInfo.DatabaseName dlc_database \
    --TableBaseInfo.TableName autotest_table_iceberg \
    --TableBaseInfo.DatasourceConnectionName DataLakeCatalog \
    --TableBaseInfo.TableComment autotest_default_comment \
    --TableBaseInfo.Type  \
    --TableBaseInfo.TableFormat  \
    --TableBaseInfo.UserAlias  \
    --TableBaseInfo.UserSubUin 100017140401 \
    --Columns.0.Name ID \
    --Columns.0.Type int \
    --Columns.0.Comment  \
    --Columns.0.Default  \
    --Columns.0.NotNull False \
    --Columns.0.Precision 0 \
    --Columns.0.Scale 0 \
    --Columns.1.Name Year \
    --Columns.1.Type int \
    --Columns.1.Comment  \
    --Columns.1.Default  \
    --Columns.1.NotNull False \
    --Columns.1.Precision 0 \
    --Columns.1.Scale 0 \
    --Columns.2.Name Month \
    --Columns.2.Type int \
    --Columns.2.Comment  \
    --Columns.2.Default  \
    --Columns.2.NotNull False \
    --Columns.2.Precision 0 \
    --Columns.2.Scale 0
```

Output: 
```
{
    "Response": {
        "Execution": {
            "SQL": "<create sql>"
        },
        "RequestId": "1882913b-70a6-4321-bd3b-50b26d1d8bed"
    }
}
```

