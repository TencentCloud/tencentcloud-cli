**Example 1: 异步预览表信息**



Input: 

```
tccli wedata DescribeTableContentPreview --cli-unfold-argument  \
    --TableId lr_At9jPStaeO9p_wMYjsQ \
    --TechnologyType ICEBERG \
    --ClusterId emr-dbcygrxq \
    --ResourceType TABLE \
    --TableName t1 \
    --ProjectId 2566642341118603264 \
    --DatabaseName worinimao
```

Output: 
```
{
    "Response": {
        "RequestId": "req_id_***",
        "ColumnNames": [
            "col1",
            "col2",
            "col3",
            "pt_day"
        ],
        "TableRecordSet": [
            {
                "TableRecordFieldSet": [
                    {
                        "Name": "col1",
                        "Value": "value1"
                    },
                    {
                        "Name": "col2",
                        "Value": "value2"
                    },
                    {
                        "Name": "col3",
                        "Value": "value3"
                    },
                    {
                        "Name": "pt_day",
                        "Value": "2026-03-10"
                    }
                ]
            },
            {
                "TableRecordFieldSet": [
                    {
                        "Name": "col1",
                        "Value": "value4"
                    },
                    {
                        "Name": "col2",
                        "Value": "value5"
                    },
                    {
                        "Name": "col3",
                        "Value": "value6"
                    },
                    {
                        "Name": "pt_day",
                        "Value": "2026-03-10"
                    }
                ]
            }
        ],
        "TaskId": "123000",
        "AsyncState": null
    }
}
```

