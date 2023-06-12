**Example 1: 获取错误日志**

获取指定时间范围内实例的错误日志。

Input: 

```
tccli postgres DescribeDBErrlogs --cli-unfold-argument  \
    --EndTime 2018-06-11 17:06:38 \
    --DBInstanceId postgres-apzvwncr \
    --StartTime 2018-06-10 17:06:38
```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "RequestId": "061bdcc0-6845-431a-a85e-ff591a352760",
        "Details": [
            {
                "UserName": "postgres",
                "ErrTime": "2018-06-22 15:22:52",
                "ErrMsg": "WARNING:  there is no transaction in progress ",
                "Database": "dee"
            },
            {
                "UserName": "postgres",
                "ErrTime": "2018-06-22 15:22:52",
                "ErrMsg": "WARNING:  there is no transaction in progress ",
                "Database": "dee"
            },
            {
                "UserName": "postgres",
                "ErrTime": "2018-06-22 15:23:09",
                "ErrMsg": "WARNING:  there is no transaction in progress ",
                "Database": "dee"
            },
            {
                "UserName": "postgres",
                "ErrTime": "2018-06-22 15:23:10",
                "ErrMsg": "WARNING:  there is no transaction in progress ",
                "Database": "dee"
            },
            {
                "UserName": "postgres",
                "ErrTime": "2018-06-22 15:23:10",
                "ErrMsg": "WARNING:  there is no transaction in progress ",
                "Database": "dee"
            },
            {
                "UserName": "postgres",
                "ErrTime": "2018-06-22 15:23:11",
                "ErrMsg": "WARNING:  there is no transaction in progress ",
                "Database": "dee"
            },
            {
                "UserName": "postgres",
                "ErrTime": "2018-06-22 15:23:11",
                "ErrMsg": "WARNING:  there is no transaction in progress ",
                "Database": "dee"
            },
            {
                "UserName": "postgres",
                "ErrTime": "2018-06-22 15:23:29",
                "ErrMsg": "WARNING:  there is no transaction in progress ",
                "Database": "dee"
            },
            {
                "UserName": "root",
                "ErrTime": "2018-06-22 15:25:01",
                "ErrMsg": "ERROR:  canceling autovacuum task CONTEXT:  automatic analyze of table \"dee.public.orders\" ",
                "Database": "dee"
            },
            {
                "UserName": "root",
                "ErrTime": "2018-06-22 15:25:10",
                "ErrMsg": "ERROR:  canceling autovacuum task CONTEXT:  automatic analyze of table \"dee.public.partsupp\" ",
                "Database": "dee"
            }
        ]
    }
}
```

