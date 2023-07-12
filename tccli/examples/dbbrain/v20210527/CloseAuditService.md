**Example 1: 关闭数据库审计**

不使用审计日志时，关闭数据库审计

Input: 

```
tccli dbbrain CloseAuditService --cli-unfold-argument  \
    --Product dcdb \
    --NodeRequestType dcdb \
    --InstanceId tdsqlsdfsd
```

Output: 
```
{
    "Response": {
        "TaskId": 0,
        "RequestId": "b39db780-0b49-11ee-8525-17d65d16bdaf"
    }
}
```

