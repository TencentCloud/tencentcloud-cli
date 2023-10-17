**Example 1: 示例1**

获取字段类型列表

Input: 

```
tccli wedata DescribeDataTypes --cli-unfold-argument  \
    --DatasourceType abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "TypeInfoSet": [
            {
                "Value": "FUNCTION",
                "Text": "函数"
            },
            {
                "Value": "CONSTANT",
                "Text": "常量"
            },
            {
                "Value": "boolean",
                "Text": "boolean"
            },
            {
                "Value": "date",
                "Text": "date"
            },
            {
                "Value": "double",
                "Text": "double"
            },
            {
                "Value": "float",
                "Text": "float"
            },
            {
                "Value": "tinyint",
                "Text": "tinyint"
            },
            {
                "Value": "smallint",
                "Text": "smallint"
            },
            {
                "Value": "tinyint unsigned",
                "Text": "tinyint unsigned"
            },
            {
                "Value": "int",
                "Text": "int"
            },
            {
                "Value": "mediumint",
                "Text": "mediumint"
            },
            {
                "Value": "smallint unsigned",
                "Text": "smallint unsigned"
            },
            {
                "Value": "Bigint",
                "Text": "Bigint"
            },
            {
                "Value": "int unsigned",
                "Text": "int unsigned"
            },
            {
                "Value": "bigint unsigned",
                "Text": "bigint unsigned"
            },
            {
                "Value": "double precision",
                "Text": "double precision"
            },
            {
                "Value": "tinyint(1)",
                "Text": "tinyint(1)"
            },
            {
                "Value": "char",
                "Text": "char"
            },
            {
                "Value": "varchar",
                "Text": "varchar"
            },
            {
                "Value": "text",
                "Text": "text"
            },
            {
                "Value": "varbinary",
                "Text": "varbinary"
            },
            {
                "Value": "blob",
                "Text": "blob"
            }
        ]
    }
}
```

