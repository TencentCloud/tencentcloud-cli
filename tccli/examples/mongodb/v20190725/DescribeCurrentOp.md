**Example 1: 查询云数据库实例的当前操作**

查询云数据库实例的当前操作

Input: 

```
tccli mongodb DescribeCurrentOp --cli-unfold-argument  \
    --InstanceId cmgo-r3p8**** \
    --State primary
```

Output: 
```
{
    "Response": {
        "CurrentOps": [
            {
                "ExecNode": "主节点",
                "MicrosecsRunning": 103,
                "NodeName": "**.**.**.**:****:*********",
                "Ns": "admin.$cmd.aggregate",
                "Op": "command",
                "OpId": 42431451,
                "Operation": "{\"Active\":true,\"AppName\":\"CMongo\",\"Client\":\"**.**.**.**:**\",\"ClientMetadata\":{\"application\":{\"name\":\"CMongo\"},\"driver\":{\"name\":\"mongo-go-driver\",\"version\":\"v1.*.*\"},\"os\":{\"architecture\":\"amd64\",\"type\":\"linux\"},\"platform\":\"***.**.*\"},\"Command\":{\"$db\":\"admin\",\"$readPreference\":{\"mode\":\"primaryPreferred\"},\"currentOp\":1,\"lsid\":{\"id\":{\"Data\":\"************************==\",\"Subtype\":4}},\"microsecs_running\":{\"$gt\":0}},\"ConnectionId\":********,\"CurrentOpTime\":\"2025-09-25T17:41:42.146+0800\",\"Desc\":\"conn*******\",\"Host\":\"*******64.site:7029\",\"Insert\":null,\"KillPending\":false,\"LockStats\":{},\"Locks\":{},\"Lsid\":{\"id\":{\"Data\":\"*******************==\",\"Subtype\":4},\"uid\":{\"Data\":\"********************************=\",\"Subtype\":0}},\"MicroSecsRunning\":103,\"Msg\":\"\",\"Ns\":\"admin.$cmd.aggregate\",\"NumYields\":0,\"Op\":\"command\",\"OpId\":********,\"OriginatingCommand\":null,\"PlanSummary\":\"\",\"Progress\":null,\"Query\":null,\"SecsRunning\":0,\"Transaction\":null,\"WaitingForLock\":false}",
                "Query": "{\"$db\":\"admin\",\"$readPreference\":{\"mode\":\"primaryPreferred\"},\"currentOp\":1,\"lsid\":{\"id\":{\"Data\":\"***********************==\",\"Subtype\":4}},\"microsecs_running\":{\"$gt\":0}}",
                "ReplicaSetName": "cmgo-r3p8****_0",
                "State": "primary"
            }
        ],
        "RequestId": "a1f20aaa-83c2-4062-b4f3-7c46ad2e1157",
        "TotalCount": 1
    }
}
```

