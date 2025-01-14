**Example 1: 获取表信息**

获取demo库下test表的表信息

Input: 

```
tccli cdwdoris DescribeTable --cli-unfold-argument  \
    --InstanceId cdwdoris-bjizjxxx \
    --DbName demo \
    --TableName table_add_table
```

Output: 
```
{
    "Response": {
        "Columns": [
            {
                "AggType": "",
                "AutoInc": false,
                "Comment": "用户id",
                "DefaultValue": "",
                "IsDistribution": true,
                "IsKey": true,
                "IsNull": false,
                "IsPartition": false,
                "Name": "user_id",
                "Type": "LARGEINT"
            },
            {
                "AggType": "",
                "AutoInc": false,
                "Comment": "数据灌入日期时间",
                "DefaultValue": "",
                "IsDistribution": false,
                "IsKey": true,
                "IsNull": false,
                "IsPartition": true,
                "Name": "date",
                "Type": "DATE"
            },
            {
                "AggType": "",
                "AutoInc": false,
                "Comment": "用户所在城市",
                "DefaultValue": "",
                "IsDistribution": false,
                "IsKey": true,
                "IsNull": true,
                "IsPartition": false,
                "Name": "city",
                "Type": "VARCHAR(20)"
            },
            {
                "AggType": "REPLACE",
                "AutoInc": false,
                "Comment": "用户最后一次访问时间",
                "DefaultValue": "1970-01-01 00:00:00",
                "IsDistribution": false,
                "IsKey": false,
                "IsNull": false,
                "IsPartition": false,
                "Name": "last_visit_date",
                "Type": "DATETIME"
            },
            {
                "AggType": "SUM",
                "AutoInc": false,
                "Comment": "用户总消费",
                "DefaultValue": "0",
                "IsDistribution": false,
                "IsKey": false,
                "IsNull": false,
                "IsPartition": false,
                "Name": "cost",
                "Type": "BIGINT"
            }
        ],
        "Distribution": {
            "Count": 3,
            "DistributionType": "Hash"
        },
        "KeysType": "AGG_KEY",
        "Message": "",
        "Partition": {
            "AutoPartition": false,
            "ListInfos": null,
            "PartitionType": "Range",
            "RangeInfos": [
                {
                    "Left": "",
                    "Max": "(\"2017-02-01\")",
                    "PartitionName": "0201",
                    "RangeType": "LESS THAN",
                    "Right": "",
                    "StepLength": 0,
                    "Unit": ""
                },
                {
                    "Left": "(\"2011-02-01\")",
                    "Max": "",
                    "PartitionName": "0202",
                    "RangeType": "FIXED",
                    "Right": "(\"2012-02-01\")",
                    "StepLength": 0,
                    "Unit": ""
                }
            ]
        },
        "Properties": [
            {
                "PropertyKey": "replication_allocation",
                "PropertyValue": "tag.location.default: 1"
            }
        ],
        "RequestId": "f4f99674-26f1-49c9-86eb-40f146f26b97",
        "TableComment": "example"
    }
}
```

