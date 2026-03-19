**Example 1: 列出血缘中心字段信息**

列出血缘中心字段信息

Input: 

```
tccli wedata DescribeLineageColumns --cli-unfold-argument  \
    --TableId GXCyOE2-TGeJjjihf5oY_A
```

Output: 
```
{
    "Response": {
        "ColumnSet": [
            {
                "TableId": "GXCyOE2-TGeJjjihf5oY_A",
                "ParentId": "10",
                "Params": "",
                "MetastoreType": "1",
                "RelationParams": "",
                "QualifiedName": "",
                "Description": "",
                "TableName": "name",
                "ColumnNameCn": "",
                "ParentSet": "",
                "ChildSet": "",
                "ColumnType": "",
                "UpStreamCount": 0,
                "PrefixPath": "",
                "DatasourceId": "",
                "ModifyTime": "",
                "MetastoreTypeName": "",
                "Tasks": [
                    ""
                ],
                "DownStreamCount": 0,
                "ExtParams": [
                    {
                        "Name": "",
                        "Value": ""
                    }
                ],
                "Id": "",
                "ColumnName": "",
                "CreateTime": ""
            }
        ],
        "TableName": "name",
        "RequestId": "",
        "MetastoreTypeName": "",
        "MetastoreType": [
            ""
        ]
    }
}
```

