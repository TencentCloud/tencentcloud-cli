**Example 1: 查询表列信息**

查询表列信息

Input: 

```
tccli wedata GetTableColumns --cli-unfold-argument  \
    --TableGuid byV1bs2QGzbTepNlHhi2gA
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Description": "",
                "IsPartition": false,
                "Length": 0,
                "Name": "tinyint_col",
                "Position": 0,
                "Type": "tinyint"
            },
            {
                "Description": "",
                "IsPartition": false,
                "Length": 0,
                "Name": "smallint_col",
                "Position": 1,
                "Type": "smallint"
            },
            {
                "Description": "",
                "IsPartition": false,
                "Length": 0,
                "Name": "int_col",
                "Position": 2,
                "Type": "int"
            },
            {
                "Description": "",
                "IsPartition": false,
                "Length": 0,
                "Name": "bigint_col",
                "Position": 3,
                "Type": "bigint"
            },
            {
                "Description": "",
                "IsPartition": false,
                "Length": 0,
                "Name": "boolean_col",
                "Position": 4,
                "Type": "boolean"
            },
            {
                "Description": "",
                "IsPartition": false,
                "Length": 0,
                "Name": "float_col",
                "Position": 5,
                "Type": "float"
            },
            {
                "Description": "",
                "IsPartition": false,
                "Length": 0,
                "Name": "double_col",
                "Position": 6,
                "Type": "double"
            },
            {
                "Description": "",
                "IsPartition": false,
                "Length": 0,
                "Name": "string_col",
                "Position": 7,
                "Type": "string"
            },
            {
                "Description": "",
                "IsPartition": false,
                "Length": 0,
                "Name": "timestamp_col",
                "Position": 8,
                "Type": "timestamp"
            },
            {
                "Description": "",
                "IsPartition": false,
                "Length": 0,
                "Name": "decimal_col",
                "Position": 9,
                "Type": "decimal(10,2)"
            },
            {
                "Description": "",
                "IsPartition": true,
                "Length": 0,
                "Name": "date_col",
                "Position": 10000,
                "Type": "date"
            }
        ],
        "RequestId": "386ce7d5-5828-4b07-9e77-58a6bc311a6d"
    }
}
```

**Example 2: OpenAPI-查询表列信息**

OpenAPI-查询表列信息

Input: 

```
tccli wedata GetTableColumns --cli-unfold-argument  \
    --TableGuid bONctN4uSTN9qL_im1kfYA
```

Output: 
```
{
    "Response": {
        "Data": [],
        "RequestId": "e4f9c44d-a371-462c-9f4a-d294421d5ab4"
    }
}
```

