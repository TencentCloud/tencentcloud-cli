**Example 1: 创建数据导入任务**



Input: 

```
tccli cdb CreateDBImportJob --cli-unfold-argument  \
    --InstanceId cdb-ids6j1b3 \
    --Password xxxxxxxxxx \
    --User xxxxx \
    --FileName test.sql
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "AsyncRequestId": "be9f64a6-fa652dc6-f5c878b6-a6a50746"
    }
}
```

**Example 2: 使用COS地址创建数据导入任务**



Input: 

```
tccli cdb CreateDBImportJob --cli-unfold-argument  \
    --InstanceId cdb-ids6j1b3 \
    --CosUrl https://test-bulk-XXXXX.cos.ap-chengdu.myqcloud.com/myFile/create_db.sql \
    --Password xxxxxxxxxx \
    --User xxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "AsyncRequestId": "be9f64a6-fa652dc6-f5c878b6-a6a50746"
    }
}
```

