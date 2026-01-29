**Example 1: 查询所有表信息**



Input: 

```
tccli tcb DescribeTables --cli-unfold-argument  \
    --MgoOffset 0 \
    --MgoLimit 20 \
    --Tag tnt-xxxxxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "4ce5365a-af8c-4859-a0dd-a4bfe1f2a3d8",
        "Tables": [
            {
                "TableName": "adise",
                "Count": 12,
                "Size": 899,
                "IndexCount": 1,
                "IndexSize": 36864
            },
            {
                "TableName": "test2",
                "Count": 1,
                "Size": 36,
                "IndexCount": 1,
                "IndexSize": 16384
            },
            {
                "TableName": "test3",
                "Count": 0,
                "Size": 0,
                "IndexCount": 1,
                "IndexSize": 4096
            },
            {
                "TableName": "test4",
                "Count": 0,
                "Size": 0,
                "IndexCount": 1,
                "IndexSize": 4096
            }
        ],
        "Pager": {
            "Offset": 0,
            "Limit": 20,
            "Total": 4
        }
    }
}
```

