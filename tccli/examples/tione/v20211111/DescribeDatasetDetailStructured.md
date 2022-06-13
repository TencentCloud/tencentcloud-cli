**Example 1: 查询结构化数据集详情**



Input: 

```
tccli tione DescribeDatasetDetailStructured --cli-unfold-argument  \
    --DatasetId ds-lpjvdzlj \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 36,
        "ColumnNames": [
            "RowId",
            "Uuid",
            "f_bool_1",
            "f_bool_2",
            "f_n_0",
            "f_int_0"
        ],
        "RowItems": [
            {
                "Values": [
                    {
                        "Name": "RowId",
                        "Value": "1"
                    },
                    {
                        "Name": "Uuid",
                        "Value": "35dvp3ziv2ww"
                    },
                    {
                        "Name": "f_bool_1",
                        "Value": "True"
                    },
                    {
                        "Name": "f_bool_2",
                        "Value": "False"
                    },
                    {
                        "Name": "f_n_0",
                        "Value": "59"
                    },
                    {
                        "Name": "f_int_0",
                        "Value": "1"
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    }
                ]
            },
            {
                "Values": [
                    {
                        "Name": "RowId",
                        "Value": "2"
                    },
                    {
                        "Name": "Uuid",
                        "Value": "35dvp3ziv2wx"
                    },
                    {
                        "Name": "f_bool_1",
                        "Value": "True"
                    },
                    {
                        "Name": "f_bool_2",
                        "Value": "True"
                    },
                    {
                        "Name": "f_n_0",
                        "Value": "89"
                    },
                    {
                        "Name": "f_int_0",
                        "Value": "2"
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    }
                ]
            },
            {
                "Values": [
                    {
                        "Name": "RowId",
                        "Value": "3"
                    },
                    {
                        "Name": "Uuid",
                        "Value": "35dvp3ziv2wy"
                    },
                    {
                        "Name": "f_bool_1",
                        "Value": "False"
                    },
                    {
                        "Name": "f_bool_2",
                        "Value": "True"
                    },
                    {
                        "Name": "f_n_0",
                        "Value": "28"
                    },
                    {
                        "Name": "f_int_0",
                        "Value": "3"
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    }
                ]
            },
            {
                "Values": [
                    {
                        "Name": "RowId",
                        "Value": "4"
                    },
                    {
                        "Name": "Uuid",
                        "Value": "35dvp3ziv2wz"
                    },
                    {
                        "Name": "f_bool_1",
                        "Value": "True"
                    },
                    {
                        "Name": "f_bool_2",
                        "Value": "True"
                    },
                    {
                        "Name": "f_n_0",
                        "Value": "8"
                    },
                    {
                        "Name": "f_int_0",
                        "Value": "7"
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    }
                ]
            },
            {
                "Values": [
                    {
                        "Name": "RowId",
                        "Value": "5"
                    },
                    {
                        "Name": "Uuid",
                        "Value": "35dvp3ziv2x0"
                    },
                    {
                        "Name": "f_bool_1",
                        "Value": "False"
                    },
                    {
                        "Name": "f_bool_2",
                        "Value": "True"
                    },
                    {
                        "Name": "f_n_0",
                        "Value": "90"
                    },
                    {
                        "Name": "f_int_0",
                        "Value": "4"
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    }
                ]
            },
            {
                "Values": [
                    {
                        "Name": "RowId",
                        "Value": "6"
                    },
                    {
                        "Name": "Uuid",
                        "Value": "35dvp3ziv2x1"
                    },
                    {
                        "Name": "f_bool_1",
                        "Value": "False"
                    },
                    {
                        "Name": "f_bool_2",
                        "Value": "False"
                    },
                    {
                        "Name": "f_n_0",
                        "Value": "21"
                    },
                    {
                        "Name": "f_int_0",
                        "Value": "9"
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    }
                ]
            },
            {
                "Values": [
                    {
                        "Name": "RowId",
                        "Value": "7"
                    },
                    {
                        "Name": "Uuid",
                        "Value": "35dvp3ziv2x2"
                    },
                    {
                        "Name": "f_bool_1",
                        "Value": "False"
                    },
                    {
                        "Name": "f_bool_2",
                        "Value": "False"
                    },
                    {
                        "Name": "f_n_0",
                        "Value": "10"
                    },
                    {
                        "Name": "f_int_0",
                        "Value": "5"
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    }
                ]
            },
            {
                "Values": [
                    {
                        "Name": "RowId",
                        "Value": "8"
                    },
                    {
                        "Name": "Uuid",
                        "Value": "35dvp3ziv2x3"
                    },
                    {
                        "Name": "f_bool_1",
                        "Value": "True"
                    },
                    {
                        "Name": "f_bool_2",
                        "Value": "True"
                    },
                    {
                        "Name": "f_n_0",
                        "Value": "76"
                    },
                    {
                        "Name": "f_int_0",
                        "Value": "2"
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    }
                ]
            },
            {
                "Values": [
                    {
                        "Name": "RowId",
                        "Value": "9"
                    },
                    {
                        "Name": "Uuid",
                        "Value": "35dvp3ziv2x4"
                    },
                    {
                        "Name": "f_bool_1",
                        "Value": "True"
                    },
                    {
                        "Name": "f_bool_2",
                        "Value": "False"
                    },
                    {
                        "Name": "f_n_0",
                        "Value": "53"
                    },
                    {
                        "Name": "f_int_0",
                        "Value": "2"
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    }
                ]
            },
            {
                "Values": [
                    {
                        "Name": "RowId",
                        "Value": "10"
                    },
                    {
                        "Name": "Uuid",
                        "Value": "35dvp3ziv2x5"
                    },
                    {
                        "Name": "f_bool_1",
                        "Value": "False"
                    },
                    {
                        "Name": "f_bool_2",
                        "Value": "False"
                    },
                    {
                        "Name": "f_n_0",
                        "Value": "78"
                    },
                    {
                        "Name": "f_int_0",
                        "Value": "3"
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Value": ""
                    }
                ]
            }
        ],
        "RowTexts": [],
        "RequestId": "afb0bc4c-5cd0-480b-bde3-5fce48158ad7"
    }
}
```

