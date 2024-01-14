**Example 1: 查询表行数**



Input: 

```
tccli cdb DescribeMysqlTableRows --cli-unfold-argument  \
    --Operator op_user \
    --AppIdUser 251051041 \
    --InstanceId cdb-0mu6taqx \
    --DBName test_1 \
    --TableName whitelist
```

Output: 
```
{
    "Response": {
        "TableRows": 10,
        "RequestId": "cafebabe-bf9cc173-222e031e-dddd"
    }
}
```

