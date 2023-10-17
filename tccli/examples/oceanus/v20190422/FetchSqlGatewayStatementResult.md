**Example 1: 查询Statement执行结果**

查询Statement执行结果

Input: 

```
tccli oceanus FetchSqlGatewayStatementResult --cli-unfold-argument  \
    --ClusterId abc \
    --SessionId abc \
    --OperationHandleId abc \
    --ResultUri abc
```

Output: 
```
{
    "Response": {
        "ErrorMessage": [
            "abc"
        ],
        "ResultType": "abc",
        "IsQueryResult": true,
        "ResultKind": "abc",
        "Results": {
            "Columns": [
                {
                    "Name": "abc",
                    "LogicalType": {
                        "Type": "abc",
                        "NullAble": true,
                        "Length": 0
                    },
                    "Comment": "abc"
                }
            ],
            "RowFormat": "abc",
            "Data": [
                {
                    "Kind": "abc",
                    "Fields": [
                        "abc"
                    ]
                }
            ]
        },
        "NextResultUri": "abc",
        "RequestId": "abc"
    }
}
```

