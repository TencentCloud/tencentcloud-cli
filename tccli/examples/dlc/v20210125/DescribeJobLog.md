**Example 1: 查询作业日志**



Input: 

```
tccli dlc DescribeJobLog --cli-unfold-argument  \
    --JobId job-9f3a2b1c \
    --LogType SPARK_SQL_OPERATION \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Lines": [
            "26/01/01 12:41:16 INFO SparkContext: Running Spark version 3.5.5"
        ],
        "Cursor": "eyJvZmZzZXQiOjEwMH0=",
        "HasMore": true,
        "Results": [
            {
                "Time": 1767256876123,
                "LogJson": "{\"level\":\"INFO\",\"message\":\"SparkContext: Running Spark version 3.5.5\"}"
            }
        ],
        "RequestId": "f4a1c9b2-7d3e-4a58-9c62-1e8b5d7a2f43"
    }
}
```

