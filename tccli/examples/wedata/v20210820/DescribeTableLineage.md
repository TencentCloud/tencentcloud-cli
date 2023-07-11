**Example 1: 列出表血缘信息**

列出表血缘信息

Input: 

```
tccli wedata DescribeTableLineage --cli-unfold-argument  \
    --Direction xx \
    --InputDepth 0 \
    --ExtParams.0.Name xx \
    --ExtParams.0.Value xx \
    --OutputDepth 0 \
    --IgnoreTemp True \
    --Data.ChildSet xx \
    --Data.Tasks xx \
    --Data.Description xx \
    --Data.DownStreamCount 0 \
    --Data.ProjectId xx \
    --Data.ExtParams.0.Name xx \
    --Data.ExtParams.0.Value xx \
    --Data.MetastoreType xx \
    --Data.TableName xx \
    --Data.QualifiedName xx \
    --Data.CreateTime xx \
    --Data.UpStreamCount 0 \
    --Data.PrefixPath xx \
    --Data.Params.0.Name xx \
    --Data.Params.0.Value xx \
    --Data.DatasourceId xx \
    --Data.ModifyTime xx \
    --Data.TableId xx \
    --Data.ParentSet xx \
    --Data.Id xx \
    --Data.MetastoreTypeName xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "TableLineage": {
            "ChildSet": "xx",
            "Tasks": [
                "xx"
            ],
            "Description": "xx",
            "DownStreamCount": 0,
            "ProjectId": "xx",
            "ExtParams": [
                {
                    "Name": "xx",
                    "Value": "xx"
                }
            ],
            "MetastoreType": "xx",
            "TableName": "xx",
            "QualifiedName": "xx",
            "CreateTime": "xx",
            "UpStreamCount": 0,
            "PrefixPath": "xx",
            "Params": [
                {
                    "Name": "xx",
                    "Value": "xx"
                }
            ],
            "DatasourceId": "xx",
            "ModifyTime": "xx",
            "TableId": "xx",
            "ParentSet": "xx",
            "Id": "xx",
            "MetastoreTypeName": "xx"
        }
    }
}
```

