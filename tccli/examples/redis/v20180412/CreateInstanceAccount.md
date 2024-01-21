**Example 1: 请求示例**



Input: 

```
tccli redis CreateInstanceAccount --cli-unfold-argument  \
    --InstanceId crs-evst**** \
    --AccountName redis_dev \
    --AccountPassword c1evuh**** \
    --ReadonlyPolicy master \
    --Privilege rw \
    --Remark "开发账号"
```

Output: 
```
{
    "Response": {
        "TaskId": 114805324,
        "RequestId": "2cd067fd-71db-4d8f-b0ac-4e83********"
    }
}
```

