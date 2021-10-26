**Example 1: 批量修改数据库实例参数**

批量修改数据库实例参数

Input: 

```
tccli postgres ModifyDBInstanceParameters --cli-unfold-argument  \
    --DBInstanceId postgres-nbvqjlhf \
    --ParamList.0.Name vacuum_freeze_table_age \
    --ParamList.0.ExpectedValue 1500000 \
    --ParamList.1.Name autovacuum_multixact_freeze_max_age \
    --ParamList.1.ExpectedValue 40000000
```

Output: 
```
{
    "Response": {
        "RequestId": "13123123123123"
    }
}
```

