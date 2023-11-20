**Example 1: 查询账户关联的数据库名称**



Input: 

```
tccli sqlserver DescribeDatabaseNames --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl \
    --AccountName account11
```

Output: 
```
{
    "Response": {
        "DatabaseNameSet": [
            "dbtest2",
            "dbtest1",
            "db2234"
        ],
        "RequestId": "ba3f44bd-6006-495d-a83c-42b166bdad21",
        "TotalCount": 3
    }
}
```

