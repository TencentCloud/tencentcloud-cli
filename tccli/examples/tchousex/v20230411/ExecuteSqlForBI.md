**Example 1: ExecuteSqlForBI**

BI侧查询sql语句

Input: 

```
tccli tchousex ExecuteSqlForBI --cli-unfold-argument  \
    --DbType test \
    --Cluster test \
    --Sql test \
    --SqlToken test \
    --Host test
```

Output: 
```
{
    "Response": {
        "InstanceId": "test",
        "ErrorMsg": "test",
        "ReturnData": "test",
        "RequestId": "test"
    }
}
```

