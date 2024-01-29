**Example 1: demo_1**

读取第一行作为字段名

Input: 

```
tccli wedata PreviewDataTableCsv --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --BucketName jaydenjhu-1315051789 \
    --FilePath /datastudio/data_manage/import/1460947878944567296/110101000000.csv \
    --HeaderLine True \
    --ColumnDelimiter 4
```

Output: 
```
{
    "Response": {
        "Data": {
            "ColumnCount": 5,
            "Columns": [
                {
                    "ColumnNumber": 1,
                    "Value": "code"
                },
                {
                    "ColumnNumber": 2,
                    "Value": "name"
                },
                {
                    "ColumnNumber": 3,
                    "Value": "province_code"
                },
                {
                    "ColumnNumber": 4,
                    "Value": "city_code"
                },
                {
                    "ColumnNumber": 5,
                    "Value": "county_code"
                }
            ],
            "IsHeadLineSchema": true,
            "RowCount": 17,
            "Rows": [
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101001000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "东华门街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 1
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101002000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "景山街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 2
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101003000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "交道口街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 3
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101004000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "安定门街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 4
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101005000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "北新桥街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 5
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101006000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "东四街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 6
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101007000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "朝阳门街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 7
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101008000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "建国门街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 8
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101009000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "东直门街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 9
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101010000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "和平里街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 10
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101011000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "和平里街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 11
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101012000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "崇文门外街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 12
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101013000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "和平里街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 13
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101014000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "龙潭街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 14
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101015000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "体育馆路街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 15
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101016000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "天坛街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 16
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101017000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": null
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 17
                }
            ]
        },
        "RequestId": "1d01faca-6318-4c24-b45f-f16d1c32942d"
    }
}
```

**Example 2: demo_2**

第一行不是字段名，返回默认的字段名，并且行分割符为英文逗号

Input: 

```
tccli wedata PreviewDataTableCsv --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --BucketName jaydenjhu-1315051789 \
    --FilePath /datastudio/data_manage/import/1460947878944567296/110101000000.csv \
    --HeaderLine False \
    --ColumnDelimiter 4
```

Output: 
```
{
    "Response": {
        "Data": {
            "ColumnCount": 5,
            "Columns": [
                {
                    "ColumnNumber": 1,
                    "Value": "column_1"
                },
                {
                    "ColumnNumber": 2,
                    "Value": "column_2"
                },
                {
                    "ColumnNumber": 3,
                    "Value": "column_3"
                },
                {
                    "ColumnNumber": 4,
                    "Value": "column_4"
                },
                {
                    "ColumnNumber": 5,
                    "Value": "column_5"
                }
            ],
            "IsHeadLineSchema": false,
            "RowCount": 18,
            "Rows": [
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "code"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "name"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "province_code"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "city_code"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "county_code"
                        }
                    ],
                    "RowNumber": 1
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101001000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "东华门街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 2
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101002000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "景山街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 3
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101003000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "交道口街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 4
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101004000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "安定门街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 5
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101005000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "北新桥街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 6
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101006000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "东四街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 7
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101007000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "朝阳门街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 8
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101008000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "建国门街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 9
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101009000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "东直门街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 10
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101010000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "和平里街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 11
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101011000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "和平里街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 12
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101012000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "崇文门外街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 13
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101013000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "和平里街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 14
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101014000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "龙潭街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 15
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101015000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "体育馆路街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 16
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101016000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": "天坛街道"
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 17
                },
                {
                    "ColumnValues": [
                        {
                            "ColumnNumber": 1,
                            "Value": "110101017000"
                        },
                        {
                            "ColumnNumber": 2,
                            "Value": null
                        },
                        {
                            "ColumnNumber": 3,
                            "Value": "11"
                        },
                        {
                            "ColumnNumber": 4,
                            "Value": "110100000000"
                        },
                        {
                            "ColumnNumber": 5,
                            "Value": "110101000000"
                        }
                    ],
                    "RowNumber": 18
                }
            ]
        },
        "RequestId": "f1a3d310-419f-4ab3-b860-3159686fcc75"
    }
}
```

