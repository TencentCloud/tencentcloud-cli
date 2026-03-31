**Example 1: 获取数据类型**



Input: 

```
tccli wedata ListDataTypes --cli-unfold-argument  \
    --DatasourceType MYSQL \
    --WorkspaceId test-project-001
```

Output: 
```
{
    "Response": {
        "Data": {
            "TypeInfoSet": [
                {
                    "Text": "常量",
                    "Value": "constant"
                },
                {
                    "Text": "函数",
                    "Value": "function"
                },
                {
                    "Text": "参数",
                    "Value": "variable"
                },
                {
                    "Text": "string",
                    "Value": "string"
                },
                {
                    "Text": "boolean",
                    "Value": "boolean"
                },
                {
                    "Text": "date",
                    "Value": "date"
                },
                {
                    "Text": "datetime",
                    "Value": "datetime"
                },
                {
                    "Text": "timestamp",
                    "Value": "timestamp"
                },
                {
                    "Text": "time",
                    "Value": "time"
                },
                {
                    "Text": "double",
                    "Value": "double"
                },
                {
                    "Text": "float",
                    "Value": "float"
                },
                {
                    "Text": "tinyint",
                    "Value": "tinyint"
                },
                {
                    "Text": "smallint",
                    "Value": "smallint"
                },
                {
                    "Text": "tinyint unsigned",
                    "Value": "tinyint unsigned"
                },
                {
                    "Text": "int",
                    "Value": "int"
                },
                {
                    "Text": "mediumint",
                    "Value": "mediumint"
                },
                {
                    "Text": "smallint unsigned",
                    "Value": "smallint unsigned"
                },
                {
                    "Text": "bigint",
                    "Value": "bigint"
                },
                {
                    "Text": "int unsigned",
                    "Value": "int unsigned"
                },
                {
                    "Text": "bigint unsigned",
                    "Value": "bigint unsigned"
                },
                {
                    "Text": "double precision",
                    "Value": "double precision"
                },
                {
                    "Text": "tinyint",
                    "Value": "tinyint"
                },
                {
                    "Text": "char",
                    "Value": "char"
                },
                {
                    "Text": "varchar",
                    "Value": "varchar"
                },
                {
                    "Text": "text",
                    "Value": "text"
                },
                {
                    "Text": "varbinary",
                    "Value": "varbinary"
                },
                {
                    "Text": "blob",
                    "Value": "blob"
                },
                {
                    "Text": "自动",
                    "Value": "autodetect"
                }
            ]
        },
        "RequestId": "9d3b3673-fd20-487e-9f23-867b1ba2c309"
    }
}
```

