**Example 1: 原始数据表字段接口**

原始数据表字段接口

Input: 

```
tccli bi DescribeSourceFieldList --cli-unfold-argument  \
    --DataSourceId 0 \
    --TableName testdata \
    --Sql testdata \
    --ProjectId 1 \
    --AsyncRequest True \
    --TranId testdata \
    --DlcExtInfo testdata \
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
        "Extra": "testdata",
        "Msg": "testdata",
        "Data": {
            "List": [
                {
                    "DbName": "testdata",
                    "AliasName": "testdata",
                    "DbType": "testdata",
                    "FieldType": "testdata",
                    "Mark": "testdata",
                    "ExcelName": "testdata",
                    "DictId": 0,
                    "DictName": "testdata",
                    "TableNodeId": "testdata",
                    "TableName": "testdata",
                    "FieldComplexType": "testdata",
                    "FormatRule": "testdata",
                    "IsFilter": true,
                    "CalcType": "testdata",
                    "CalcFormula": "testdata",
                    "CalcDesc": "testdata",
                    "JsonPathName": "testdata",
                    "Granularity": "testdata"
                }
            ],
            "TranId": "testdata",
            "TranStatus": 0
        },
        "RequestId": "testdata"
    }
}
```

