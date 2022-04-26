**Example 1: 查询SQL模板**



Input: 

```
tccli dbbrain DescribeSqlTemplate --cli-unfold-argument  \
    --InstanceId cdb-test \
    --Schema test \
    --SqlText select * from test limit 10 \
    --Product mysql
```

Output: 
```
{
    "Response": {
        "RequestId": "a837a5ce-b48f-4548-9a6b-a6e0917d8e5c",
        "Schema": "test",
        "SqlText": "select * from test limit 10",
        "SqlType": "Select",
        "SqlTemplate": "select * from test limit ?",
        "SqlId": -5602209514906915428
    }
}
```

