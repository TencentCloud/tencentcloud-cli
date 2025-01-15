**Example 1: 根据sql查询**



Input: 

```
tccli cdwdoris ExecuteSelectQuery --cli-unfold-argument  \
    --InstanceId cdwdoris-xxx \
    --Database demo1 \
    --Query SELECT * FROM my_table LIMIT 10 OFFSET 0;
```

Output: 
```
{
    "Response": {
        "Fields": [
            "id",
            "name",
            "age",
            "salary",
            "join_date"
        ],
        "Rows": [
            {
                "DataRow": [
                    "11",
                    "John Doe",
                    "30",
                    "7000.50000",
                    "2024-08-27 00:00:00 +0800 CST"
                ]
            },
            {
                "DataRow": [
                    "21",
                    "Jane Smith",
                    "25",
                    "6000.00000",
                    "2024-08-28 00:00:00 +0800 CST"
                ]
            },
            {
                "DataRow": [
                    "11",
                    "John Doe",
                    "30",
                    "7000.50000",
                    "2024-08-27 00:00:00 +0800 CST"
                ]
            },
            {
                "DataRow": [
                    "21",
                    "Jane Smith",
                    "25",
                    "6000.00000",
                    "2024-08-28 00:00:00 +0800 CST"
                ]
            }
        ],
        "RequestId": "xx-xx-xx-xx-xx"
    }
}
```

