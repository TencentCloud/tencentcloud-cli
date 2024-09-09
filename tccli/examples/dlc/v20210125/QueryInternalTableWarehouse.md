**Example 1: 获取原生表warehouse路径**



Input: 

```
tccli dlc QueryInternalTableWarehouse --cli-unfold-argument  \
    --TableName db_test \
    --DatabaseName tb_test
```

Output: 
```
{
    "Response": {
        "WarehousePath": "lakefs://xxx@xxx/xxx/warehouse/db_test/tb_test/",
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

