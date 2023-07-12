**Example 1: 开通数据库审计**

开通数据库审计后，将会上报审计日志

Input: 

```
tccli dbbrain OpenAuditService --cli-unfold-argument  \
    --Product dcdb \
    --NodeRequestType dcdb \
    --InstanceId tdsqlsertsd \
    --LogExpireDay 30 \
    --HotLogExpireDay 7
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

