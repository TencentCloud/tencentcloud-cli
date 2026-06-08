**Example 1: 创建数据表**

创建数据表

Input: 

```
tccli bi CreateDataTable --cli-unfold-argument  \
    --Type 1 \
    --Name testdata \
    --FoldId 1 \
    --DatasourceId testdata \
    --TableName testdata \
    --Sql testdata \
    --ExcelUrl testdata \
    --Fields.0.DbName testdata \
    --Fields.0.AliasName testdata \
    --Fields.0.DbType testdata \
    --Fields.0.FieldType testdata \
    --Fields.0.FieldComplexType testdata \
    --Fields.0.Mark testdata \
    --Fields.0.FormatRule testdata \
    --Fields.0.IsFilter True \
    --Fields.0.CalcType testdata \
    --Fields.0.CalcFormula testdata \
    --Fields.0.CalcDesc testdata \
    --Fields.0.DictId 1 \
    --Fields.0.DictName testdata \
    --Fields.0.TableNodeId testdata \
    --Fields.0.ExcelName testdata \
    --Fields.0.TableName testdata \
    --Fields.0.JsonPathName testdata \
    --Fields.0.Granularity testdata \
    --ProjectId 1 \
    --TableNodeType 1 \
    --Tables.0.TableNodeType 1 \
    --Tables.0.TableNodeId testdata \
    --Tables.0.ParentId testdata \
    --Tables.0.TableId testdata \
    --Tables.0.TableName testdata \
    --Tables.0.Fields.0.DbName testdata \
    --Tables.0.Fields.0.AliasName testdata \
    --Tables.0.Fields.0.DbType testdata \
    --Tables.0.Fields.0.FieldType testdata \
    --Tables.0.Fields.0.FieldComplexType testdata \
    --Tables.0.Fields.0.Mark testdata \
    --Tables.0.Fields.0.FormatRule testdata \
    --Tables.0.Fields.0.IsFilter True \
    --Tables.0.Fields.0.CalcType testdata \
    --Tables.0.Fields.0.CalcFormula testdata \
    --Tables.0.Fields.0.CalcDesc testdata \
    --Tables.0.Fields.0.DictId 1 \
    --Tables.0.Fields.0.DictName testdata \
    --Tables.0.Fields.0.TableNodeId testdata \
    --Tables.0.Fields.0.ExcelName testdata \
    --Tables.0.Fields.0.TableName testdata \
    --Tables.0.Fields.0.JsonPathName testdata \
    --Tables.0.Fields.0.Granularity testdata \
    --Tables.0.DatasourceId 1 \
    --Tables.0.TableAlias testdata \
    --Joins.0.JoinId testdata \
    --Joins.0.SourceTableNodeId testdata \
    --Joins.0.TargetTableNodeId testdata \
    --Joins.0.JoinType testdata \
    --Joins.0.Fields.0.FieldJoinId testdata \
    --Joins.0.Fields.0.SourceField.DbName testdata \
    --Joins.0.Fields.0.SourceField.AliasName testdata \
    --Joins.0.Fields.0.SourceField.DbType testdata \
    --Joins.0.Fields.0.SourceField.FieldType testdata \
    --Joins.0.Fields.0.SourceField.FieldComplexType testdata \
    --Joins.0.Fields.0.SourceField.Mark testdata \
    --Joins.0.Fields.0.SourceField.FormatRule testdata \
    --Joins.0.Fields.0.SourceField.IsFilter True \
    --Joins.0.Fields.0.SourceField.CalcType testdata \
    --Joins.0.Fields.0.SourceField.CalcFormula testdata \
    --Joins.0.Fields.0.SourceField.CalcDesc testdata \
    --Joins.0.Fields.0.SourceField.DictId 1 \
    --Joins.0.Fields.0.SourceField.DictName testdata \
    --Joins.0.Fields.0.SourceField.TableNodeId testdata \
    --Joins.0.Fields.0.SourceField.ExcelName testdata \
    --Joins.0.Fields.0.SourceField.TableName testdata \
    --Joins.0.Fields.0.SourceField.JsonPathName testdata \
    --Joins.0.Fields.0.SourceField.Granularity testdata \
    --ExtInfo testdata \
    --DlcExtInfo testdata \
    --AsyncRequest True \
    --ParentTranId testdata \
    --ApiDatasourceConfig.FieldsJsonData testdata \
    --ApiDatasourceConfig.ConnectionType 1 \
    --ApiDatasourceConfig.FrequencyConfig.Frequency testdata \
    --ApiDatasourceConfig.FrequencyConfig.Dates 0 \
    --ApiDatasourceConfig.FrequencyConfig.Time testdata \
    --ApiDatasourceConfig.FrequencyConfig.IntervalTime 1 \
    --ApiDatasourceConfig.FrequencyConfig.IntervalTimeUnit 1 \
    --ApiDatasourceConfig.FrequencyConfig.Hours 0 \
    --ApiDatasourceConfig.FrequencyConfig.Minute 0 \
    --ApiDatasourceConfig.Url testdata \
    --ApiDatasourceConfig.RequestMethod 1 \
    --ApiDatasourceConfig.RequestHeader testdata \
    --ApiDatasourceConfig.RequestParams testdata \
    --ApiDatasourceConfig.RequestBody testdata \
    --ApiDatasourceConfig.UserName testdata \
    --ApiDatasourceConfig.Password testdata \
    --ApiDatasourceConfig.AuthorizationType 1 \
    --ApiDatasourceConfig.TableId 1 \
    --ApiDatasourceConfig.JsonPathDbNameMap testdata \
    --ParamList.0.ParamName testdata \
    --ParamList.0.DefaultValue testdata \
    --ParamList.0.ParamType testdata \
    --ParamList.0.FormatRule testdata \
    --ParamList.0.ComplexType testdata
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": 0,
            "AccessKey": "testdata",
            "ProjectId": 1,
            "TranId": "testdata",
            "TranStatus": 0
        },
        "Extra": "testdata",
        "Msg": "testdata",
        "RequestId": "testdata"
    }
}
```

