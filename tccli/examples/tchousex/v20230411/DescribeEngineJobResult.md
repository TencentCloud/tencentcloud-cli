**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex DescribeEngineJobResult --cli-unfold-argument  \
    --InstanceId warehouse-ooj2s44q \
    --EngineJobId tchousex-o7wg1p \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "EngineJobAsyncResult": null,
        "EngineJobResult": {
            "Charset": "utf-8",
            "ResultSet": "null"
        },
        "EngineJobResultMeta": {
            "CostTime": 0,
            "CreateTime": "1704902010000",
            "ResultSchema": [
                {
                    "Description": "",
                    "ExtParameters": null,
                    "Length": 0,
                    "Name": "l_orderkey",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "bigint"
                },
                {
                    "Description": "",
                    "ExtParameters": null,
                    "Length": 0,
                    "Name": "l_partkey",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "bigint"
                },
                {
                    "Description": "",
                    "ExtParameters": null,
                    "Length": 0,
                    "Name": "l_suppkey",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "bigint"
                },
                {
                    "Description": "",
                    "ExtParameters": null,
                    "Length": 0,
                    "Name": "l_linenumber",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "bigint"
                },
                {
                    "Description": "",
                    "ExtParameters": null,
                    "Length": 0,
                    "Name": "l_quantity",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "decimal"
                },
                {
                    "Description": "",
                    "ExtParameters": null,
                    "Length": 0,
                    "Name": "l_extendedprice",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "decimal"
                },
                {
                    "Description": "",
                    "ExtParameters": null,
                    "Length": 0,
                    "Name": "l_discount",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "decimal"
                },
                {
                    "Description": "",
                    "ExtParameters": null,
                    "Length": 0,
                    "Name": "l_tax",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "decimal"
                },
                {
                    "Description": "",
                    "ExtParameters": null,
                    "Length": 0,
                    "Name": "l_returnflag",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "string"
                },
                {
                    "Description": "",
                    "ExtParameters": null,
                    "Length": 0,
                    "Name": "l_linestatus",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "string"
                },
                {
                    "Description": "",
                    "ExtParameters": null,
                    "Length": 0,
                    "Name": "l_shipdate",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "date"
                },
                {
                    "Description": "",
                    "ExtParameters": null,
                    "Length": 0,
                    "Name": "l_commitdate",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "date"
                },
                {
                    "Description": "",
                    "ExtParameters": null,
                    "Length": 0,
                    "Name": "l_receiptdate",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "date"
                },
                {
                    "Description": "",
                    "ExtParameters": null,
                    "Length": 0,
                    "Name": "l_shipinstruct",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "string"
                },
                {
                    "Description": "",
                    "ExtParameters": null,
                    "Length": 0,
                    "Name": "l_shipmode",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "string"
                },
                {
                    "Description": "",
                    "ExtParameters": null,
                    "Length": 0,
                    "Name": "l_comment",
                    "Position": 0,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "string"
                }
            ],
            "SQL": "select * from test.lineitem limit 2000000000",
            "TotalCount": 121241201
        },
        "EngineJobResultType": 0,
        "RequestId": "38e514a1-fe43-4d7c-bc07-edc749ad9dc4"
    }
}
```

