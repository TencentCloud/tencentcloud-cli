**Example 1: 查询表信息**

查询表信息

Input: 

```
tccli dlc DescribeTable --cli-unfold-argument  \
    --TableName table2 \
    --DatabaseName database1 \
    --DatasourceConnectionName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "RequestId": "********-****-****-****-b20a8b876cfb",
        "Table": {
            "Columns": [
                {
                    "Comment": "test col",
                    "CreateTime": "1736941935000",
                    "DataMaskStrategyInfo": null,
                    "IsPartition": true,
                    "ModifiedTime": "",
                    "Name": "column1",
                    "Nullable": "",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "int"
                }
            ],
            "CreateTime": "1736853257000",
            "HeatValue": 10,
            "InputFormat": "org.apache.hadoop.mapred.FileInputFormat",
            "InputFormatShort": "parquet",
            "Location": "cosn://********",
            "ModifiedTime": "1736941935000",
            "Partitions": [
                {
                    "Comment": "test col",
                    "CreateTime": 0,
                    "Name": "column1",
                    "Transform": "identity",
                    "TransformArgs": null,
                    "Type": "int"
                }
            ],
            "Properties": [
                {
                    "Key": "comment",
                    "Value": "test comment"
                },
                {
                    "Key": "property1",
                    "Value": "test property"
                },
                {
                    "Key": "test property",
                    "Value": "default value"
                }
            ],
            "RecordCount": 0,
            "StorageSize": 0,
            "TableBaseInfo": {
                "DatabaseName": "database1",
                "DatasourceConnectionName": "",
                "DbGovernPolicyIsDisable": "",
                "GovernPolicy": {
                    "RuleType": "none"
                },
                "TableComment": null,
                "TableFormat": "ICEBERG",
                "TableName": "table2",
                "Type": "MANAGED_TABLE",
                "UserAlias": "t********",
                "UserSubUin": "1*********6"
            }
        }
    }
}
```

