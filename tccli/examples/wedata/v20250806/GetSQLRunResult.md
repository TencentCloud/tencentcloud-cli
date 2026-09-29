**Example 1: 成功响应**

查询任务已执行成功，返回两个字段、两行数据。Rows 中每个元素为一行，其 Values 顺序与 Columns 一致；单元格均为字符串（底层预览结果为 CSV 格式，不携带类型信息），字段真实类型参见 Columns[].ColumnType。

Input: 

```
tccli wedata GetSQLRunResult --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --JobId 6820250918152834057
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": "6820250918152834057",
            "Status": "SUCCESS",
            "StatusMessage": "任务执行成功，已返回全部查询结果",
            "CostMs": 10000,
            "Truncated": false,
            "Results": [
                {
                    "JobExecutionId": "6820250918152834057-1",
                    "Status": "SUCCESS",
                    "Columns": [
                        {
                            "ColumnName": "id",
                            "ColumnType": "int"
                        },
                        {
                            "ColumnName": "name",
                            "ColumnType": "string"
                        }
                    ],
                    "Rows": [
                        {
                            "Values": [
                                "1",
                                "Alice"
                            ]
                        },
                        {
                            "Values": [
                                "2",
                                null
                            ]
                        }
                    ],
                    "Total": 2,
                    "CostMs": 12,
                    "Truncated": false
                }
            ]
        },
        "RequestId": "08955a5f-497f-4bac-bac6-99c75191ffa7"
    }
}
```

**Example 2: 任务未执行完成（轮询中）**

任务仍处于非终态（QUEUED/RUNNING）时本接口不报错，返回当前 Status 与空的 Results 数组，并通过 StatusMessage 说明原因与下一步动作。调用方应据此指数退避轮询，直至 Status 变为 SUCCESS/FAILED/TERMINATED/CANCELED 之一。注意 FAILED/TERMINATED/CANCELED 同为终态且同样没有结果数据，请以 StatusMessage 判断是继续等待还是终止轮询。

Input: 

```
tccli wedata GetSQLRunResult --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --JobId 6820250918152834057
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": "6820250918152834057",
            "Status": "RUNNING",
            "StatusMessage": "任务尚未执行完成，当前无结果数据，请使用相同的 JobId 稍后重试",
            "CostMs": 3200,
            "Truncated": false,
            "Results": []
        },
        "RequestId": "1f0c2b7e-6d4a-4f31-9a55-3c1d8e02b4aa"
    }
}
```

