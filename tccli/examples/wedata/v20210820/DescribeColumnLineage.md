**Example 1: 列出表血缘信息**

列出表血缘信息

Input: 

```
tccli wedata DescribeColumnLineage --cli-unfold-argument  \
    --Direction xx \
    --InputDepth 0 \
    --ExtParams.0.Name xx \
    --ExtParams.0.Value xx \
    --OutputDepth 0 \
    --IgnoreTemp True \
    --Data.ParentId xx \
    --Data.Params xx \
    --Data.MetastoreType xx \
    --Data.RelationParams xx \
    --Data.QualifiedName xx \
    --Data.Description xx \
    --Data.TableName xx \
    --Data.ColumnNameCn xx \
    --Data.ParentSet xx \
    --Data.ChildSet xx \
    --Data.ColumnType xx \
    --Data.UpStreamCount 0 \
    --Data.PrefixPath xx \
    --Data.DatasourceId xx \
    --Data.ModifyTime xx \
    --Data.MetastoreTypeName xx \
    --Data.Tasks xx \
    --Data.DownStreamCount 0 \
    --Data.ExtParams.0.Name xx \
    --Data.ExtParams.0.Value xx \
    --Data.Id xx \
    --Data.ColumnName xx \
    --Data.TableId xx \
    --Data.CreateTime xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "ColumnAggregationLineage": {
            "ChildSet": "xx",
            "ParentSet": "xx",
            "ParentId": "xx",
            "TableName": "xx",
            "MetastoreType": "xx",
            "ColumnInfoSet": [
                {
                    "QualifiedName": "xx",
                    "Tasks": [
                        "xx"
                    ],
                    "ColumnType": "xx",
                    "Description": "xx",
                    "DownStreamCount": 0,
                    "UpStreamCount": 0,
                    "CreateTime": "xx",
                    "ColumnName": "xx",
                    "PrefixPath": "xx",
                    "Params": "xx",
                    "ModifyTime": "xx",
                    "RelationParams": "xx",
                    "ColumnNameCn": "xx",
                    "Id": "xx",
                    "DatasourceId": "xx"
                }
            ]
        }
    }
}
```

