**Example 1: 获取作业结果集**



Input: 

```
tccli dlc DescribeJobResult --cli-unfold-argument  \
    --Page 1 \
    --PageSize 10 \
    --JobId job-9f3a2b1c
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "JobId": "job-9f3a2b1c",
        "State": "SUCCEEDED",
        "Message": "OK",
        "Columns": [
            {
                "Name": "id",
                "DataType": "BIGINT",
                "Comment": "行号",
                "Nullable": true
            },
            {
                "Name": "job_name",
                "DataType": "STRING",
                "Comment": "作业名",
                "Nullable": true
            },
            {
                "Name": "state",
                "DataType": "STRING",
                "Comment": "作业状态",
                "Nullable": true
            }
        ],
        "TotalRows": 1,
        "Rows": [
            {
                "Values": [
                    "1",
                    "spark-sql-demo",
                    "SUCCEEDED"
                ]
            }
        ],
        "Truncated": false,
        "RequestId": "f4a1c9b2-7d3e-4a58-9c62-1e8b5d7a2f43"
    }
}
```

