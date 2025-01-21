**Example 1: 示例1**

查询数据表列表。

Input: 

```
tccli dlc DescribeTables --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0 \
    --DatabaseName database1 \
    --Filters.0.Name table-name \
    --Filters.0.Values table2 \
    --DatasourceConnectionName DataLakeCatalog \
    --Sort CreateTime
```

Output: 
```
{
    "Response": {
        "RequestId": "********-****-****-****-ea237088c286",
        "TableList": [
            {
                "Columns": null,
                "CreateTime": "1736853257000",
                "HeatValue": 10,
                "InputFormat": "org.apache.hadoop.mapred.FileInputFormat",
                "InputFormatShort": "parquet",
                "Location": "cosn://********",
                "ModifiedTime": "1736941935000",
                "Partitions": [
                    {
                        "Comment": "",
                        "CreateTime": 0,
                        "Name": "column1",
                        "Transform": "identity",
                        "TransformArgs": null,
                        "Type": ""
                    }
                ],
                "Properties": [
                    {
                        "Key": "property1",
                        "Value": "test property"
                    },
                    {
                        "Key": "test property",
                        "Value": "default value"
                    },
                    {
                        "Key": "metadata_location",
                        "Value": "cosn://********"
                    }
                ],
                "RecordCount": 0,
                "StorageSize": 0,
                "TableBaseInfo": {
                    "DatabaseName": "database1",
                    "DatasourceConnectionName": "",
                    "DbGovernPolicyIsDisable": "true",
                    "GovernPolicy": {
                        "RuleType": "none"
                    },
                    "TableComment": null,
                    "TableFormat": "ICEBERG",
                    "TableName": "table2",
                    "Type": "MANAGED_TABLE",
                    "UserAlias": "t**********",
                    "UserSubUin": "1**********6"
                }
            }
        ],
        "TotalCount": 1
    }
}
```

