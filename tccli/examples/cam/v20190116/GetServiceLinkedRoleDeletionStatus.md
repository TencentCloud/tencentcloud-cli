**Example 1: 获取服务相关角色删除状态**



Input: 

```
tccli cam GetServiceLinkedRoleDeletionStatus --cli-unfold-argument  \
    --DeletionTaskId 100
```

Output: 
```
{
    "Response": {
        "Status": "SUCCEEDED",
        "ServiceType": "cam",
        "ServiceName": "访问管理",
        "Reason": "{}",
        "RequestId": "c3da1c1c-df35-467d-9335-99c68d993e0a"
    }
}
```

