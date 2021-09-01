**Example 1: 查询主事务列表**



Input: 

```
tccli dtf DescribeTransactions --cli-unfold-argument  \
    --GroupId group-qy9484ln
```

Output: 
```
{
    "Response": {
        "RequestId": "e0bc66ed-c2eb-4d49-931e-18dab5c25d8a",
        "Result": {
            "TotalCount": null,
            "Content": [
                {
                    "TransactionId": 20052,
                    "TransactionBegin": 1581951071521,
                    "TransactionCommit": 1581951077545,
                    "TransactionRollback": null,
                    "TransactionEnd": null,
                    "TransactionError": 1581951077549,
                    "Timeout": 60000,
                    "Status": 1,
                    "TimeoutFlag": 0,
                    "EndFlag": 1,
                    "Comment": "Some Branches confirm failed.",
                    "BranchQuantity": 2,
                    "GroupId": "group-qy9484ln",
                    "Server": null,
                    "RetryFlag": true
                }
            ]
        }
    }
}
```

