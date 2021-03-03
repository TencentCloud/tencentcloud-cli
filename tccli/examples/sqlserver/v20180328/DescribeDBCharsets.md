**Example 1: 查询数据库字符集**



Input: 

```
tccli sqlserver DescribeDBCharsets --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl
```

Output: 
```
{
    "Response": {
        "DatabaseCharsets": [
            "SQL_EBCDIC1141_CP1_CS_AS",
            "SQL_EBCDIC277_2_CP1_CS_AS",
            "SQL_Ukrainian_CP1251_CI_AS",
            "SQL_Ukrainian_CP1251_CS_AS"
        ],
        "RequestId": "b28ec299-0063-4195-9273-ebac5cdc485c"
    }
}
```

