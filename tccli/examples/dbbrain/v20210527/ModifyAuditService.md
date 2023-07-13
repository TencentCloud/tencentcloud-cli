**Example 1: 修改审计配置**

修改审计配置，如，修改高频日志保存天数

Input: 

```
tccli dbbrain ModifyAuditService --cli-unfold-argument  \
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
        "Success": 0,
        "RequestId": "b39db780-0b49-11ee-8525-17d65d16bdaf"
    }
}
```

