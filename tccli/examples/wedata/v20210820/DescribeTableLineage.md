**Example 1: 表血缘信息**

表血缘信息

Input: 

```
tccli wedata DescribeTableLineage --cli-unfold-argument  \
    --Direction INPUT \
    --InputDepth 1 \
    --OutputDepth 1 \
    --Data.TableId nCG0n7zjR7-N-EbAAi8Ruw \
    --Data.MetastoreType HIVE \
    --Data.PrefixPath  \
    --IgnoreTemp True
```

Output: 
```
{
    "Response": {
        "RequestId": "cea6a2ea-a841-43ae-883a-805a58dc53d3",
        "TableLineage": {
            "ChildSet": "[]",
            "CreateTime": "",
            "DatasourceId": "",
            "Description": "",
            "DownStreamCount": 0,
            "ExtParams": [],
            "Id": null,
            "MetastoreType": null,
            "MetastoreTypeName": null,
            "ModifyTime": "",
            "Params": [],
            "ParentSet": "[]",
            "PrefixPath": "",
            "ProjectId": null,
            "QualifiedName": null,
            "TableId": "nCG0n7zjR7-N-EbAAi8Ruw",
            "TableName": "student",
            "Tasks": [],
            "UpStreamCount": 0
        }
    }
}
```

**Example 2: 列出表血缘信息**

列出表血缘信息

Input: 

```
tccli wedata DescribeTableLineage --cli-unfold-argument  \
    --Direction abc \
    --InputDepth 0 \
    --OutputDepth 0 \
    --ExtParams.0.Name abc \
    --ExtParams.0.Value abc \
    --Data.ProjectId abc \
    --Data.DatasourceId abc \
    --Data.TableId abc \
    --Data.Params.0.Name abc \
    --Data.Params.0.Value abc \
    --Data.ParentSet abc \
    --Data.ChildSet abc \
    --Data.ExtParams.0.Name abc \
    --Data.ExtParams.0.Value abc \
    --Data.Id abc \
    --Data.MetastoreType abc \
    --Data.MetastoreTypeName abc \
    --Data.TableName abc \
    --Data.QualifiedName abc \
    --Data.DownStreamCount 0 \
    --Data.UpStreamCount 0 \
    --Data.Description abc \
    --Data.PrefixPath abc \
    --Data.CreateTime abc \
    --Data.ModifyTime abc \
    --Data.Tasks abc \
    --IgnoreTemp True \
    --RecursiveSecond True
```

Output: 
```
{
    "Response": {
        "TableLineage": {
            "ProjectId": "abc",
            "DatasourceId": "abc",
            "TableId": "abc",
            "Params": [
                {
                    "Name": "abc",
                    "Value": "abc"
                }
            ],
            "ParentSet": "abc",
            "ChildSet": "abc",
            "ExtParams": [
                {
                    "Name": "abc",
                    "Value": "abc"
                }
            ],
            "Id": "abc",
            "MetastoreType": "abc",
            "MetastoreTypeName": "abc",
            "TableName": "abc",
            "QualifiedName": "abc",
            "DownStreamCount": 0,
            "UpStreamCount": 0,
            "Description": "abc",
            "PrefixPath": "abc",
            "CreateTime": "abc",
            "ModifyTime": "abc",
            "Tasks": [
                "abc"
            ]
        },
        "RequestId": "abc"
    }
}
```

