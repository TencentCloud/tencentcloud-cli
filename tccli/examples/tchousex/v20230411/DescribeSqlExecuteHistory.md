**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex DescribeSqlExecuteHistory --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --InstanceId warehouse-ooj2s44q \
    --UserName root
```

Output: 
```
{
    "Response": {
        "ErrMsg": "",
        "ErrorMsg": "",
        "Records": [
            {
                "ErrMsg": "",
                "ExecuteTime": 289,
                "Host": "",
                "Id": 4819,
                "InstanceId": "warehouse-ooj2s44q",
                "ScanQuantity": "",
                "Sql": "/* +engine=batch */ select 1",
                "SqlType": 1,
                "StartTime": "2024-01-18 19:06:03",
                "TaskId": "sql-task-zdaafa",
                "TaskStatus": -2,
                "UserName": "root",
                "Warehouse": "bob-test"
            },
            {
                "ErrMsg": "",
                "ExecuteTime": 280,
                "Host": "",
                "Id": 4818,
                "InstanceId": "warehouse-ooj2s44q",
                "ScanQuantity": "",
                "Sql": "/* +engine=batch */ select 1",
                "SqlType": 1,
                "StartTime": "2024-01-18 18:25:58",
                "TaskId": "",
                "TaskStatus": 8,
                "UserName": "root",
                "Warehouse": "bob-test"
            },
            {
                "ErrMsg": "",
                "ExecuteTime": 288,
                "Host": "",
                "Id": 4817,
                "InstanceId": "warehouse-ooj2s44q",
                "ScanQuantity": "",
                "Sql": "/* +engine=batch */ select 1",
                "SqlType": 1,
                "StartTime": "2024-01-18 16:53:40",
                "TaskId": "",
                "TaskStatus": 1,
                "UserName": "root",
                "Warehouse": "bob-test"
            },
            {
                "ErrMsg": "",
                "ExecuteTime": 284,
                "Host": "",
                "Id": 4816,
                "InstanceId": "warehouse-ooj2s44q",
                "ScanQuantity": "",
                "Sql": "/* +engine=batch */ select 1",
                "SqlType": 1,
                "StartTime": "2024-01-18 16:40:23",
                "TaskId": "",
                "TaskStatus": 1,
                "UserName": "root",
                "Warehouse": "bob-test"
            },
            {
                "ErrMsg": "",
                "ExecuteTime": 1241,
                "Host": "",
                "Id": 4815,
                "InstanceId": "warehouse-ooj2s44q",
                "ScanQuantity": "",
                "Sql": "/* +engine=batch */ select 1",
                "SqlType": 0,
                "StartTime": "2024-01-18 16:24:32",
                "TaskId": "tchousex-34odpz",
                "TaskStatus": 1,
                "UserName": "root",
                "Warehouse": "bob-test"
            },
            {
                "ErrMsg": "",
                "ExecuteTime": 857,
                "Host": "",
                "Id": 4814,
                "InstanceId": "warehouse-ooj2s44q",
                "ScanQuantity": "",
                "Sql": "/* +engine=batch */ select 1",
                "SqlType": 0,
                "StartTime": "2024-01-18 16:07:04",
                "TaskId": "tchousex-ckmje2",
                "TaskStatus": 1,
                "UserName": "root",
                "Warehouse": "bob-test"
            },
            {
                "ErrMsg": "",
                "ExecuteTime": 1154,
                "Host": "",
                "Id": 4813,
                "InstanceId": "warehouse-ooj2s44q",
                "ScanQuantity": "",
                "Sql": "/* +engine=batch */ select 1",
                "SqlType": 0,
                "StartTime": "2024-01-18 15:49:41",
                "TaskId": "tchousex-2xxgxl",
                "TaskStatus": 1,
                "UserName": "root",
                "Warehouse": "bob-test"
            },
            {
                "ErrMsg": "",
                "ExecuteTime": 2347,
                "Host": "",
                "Id": 4812,
                "InstanceId": "warehouse-ooj2s44q",
                "ScanQuantity": "329.84 MB",
                "Sql": "select * from test.lineitem limit 2000",
                "SqlType": 0,
                "StartTime": "2024-01-18 14:55:37",
                "TaskId": "tchousex-j8vjca",
                "TaskStatus": 1,
                "UserName": "root",
                "Warehouse": "bob-test"
            },
            {
                "ErrMsg": "",
                "ExecuteTime": 2917,
                "Host": "",
                "Id": 4811,
                "InstanceId": "warehouse-ooj2s44q",
                "ScanQuantity": "372.73 MB",
                "Sql": "select * from test.lineitem limit 2000",
                "SqlType": 0,
                "StartTime": "2024-01-18 14:25:10",
                "TaskId": "",
                "TaskStatus": 1,
                "UserName": "root",
                "Warehouse": "bob-test"
            },
            {
                "ErrMsg": "unexpected EOF",
                "ExecuteTime": 5216,
                "Host": "",
                "Id": 4807,
                "InstanceId": "warehouse-ooj2s44q",
                "ScanQuantity": "",
                "Sql": "/* +engine=batch */ select 1",
                "SqlType": 0,
                "StartTime": "2024-01-17 11:41:37",
                "TaskId": "",
                "TaskStatus": 0,
                "UserName": "root",
                "Warehouse": "bob-test"
            }
        ],
        "RequestId": "b1b7312d-edcb-465c-8ac6-e64545956f7f",
        "TotalCount": 19
    }
}
```

**Example 2: DescribeSqlExecuteHistory**

sql工作区sql执行历史记录展示

Input: 

```
tccli tchousex DescribeSqlExecuteHistory --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --InstanceId abc \
    --UserName abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ErrorMsg": "abc",
        "ErrMsg": "abc",
        "Records": [
            {
                "Id": 0,
                "InstanceId": "abc",
                "Sql": "abc",
                "UserName": "abc",
                "StartTime": "abc",
                "ExecuteTime": 0,
                "Status": true,
                "ErrMsg": "abc",
                "Host": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

