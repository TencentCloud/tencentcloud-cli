**Example 1: 查询表**



Input: 

```
tccli cdwdoris QueryTableData --cli-unfold-argument  \
    --InstanceId cdwdoris-xx \
    --Database __internal_schema \
    --Table audit_log \
    --SelectedFields query_id time stmt \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 201884,
        "Fields": [
            "query_id",
            "time",
            "stmt"
        ],
        "FieldTypes": [
            "varchar(48)",
            "datetime(3)",
            "text"
        ],
        "Rows": [
            {
                "DataRow": [
                    "101b40ffd49745f7-81390314edcbd685",
                    "2024-09-02 12:21:43.566 +0800 CST",
                    " SHOW PROC '/brokers'"
                ]
            },
            {
                "DataRow": [
                    "10206b070d714e53-860d81312913b4f9",
                    "2024-09-02 16:55:09.246 +0800 CST",
                    " SHOW PROC '/backends'"
                ]
            },
            {
                "DataRow": [
                    "10216c610b93435d-a9dab3ab3312e66a",
                    "2024-09-02 20:53:25.565 +0800 CST",
                    " SHOW PROC '/backends'"
                ]
            }
        ],
        "RequestId": "xx-xx-xx-xx-xx"
    }
}
```

