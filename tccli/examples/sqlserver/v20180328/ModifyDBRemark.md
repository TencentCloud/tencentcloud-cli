**Example 1: 修改数据库备注**



Input: 

```
tccli sqlserver ModifyDBRemark --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl \
    --DBRemarks.0.Name db_test \
    --DBRemarks.0.Remark 测试数据库
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

