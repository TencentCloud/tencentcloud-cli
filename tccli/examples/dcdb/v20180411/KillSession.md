**Example 1: 杀死指定会话**



Input: 

```
tccli dcdb KillSession --cli-unfold-argument  \
    --InstanceId tdsqlshard-2gk4nxyz \
    --ShardId shard-ljilb4st \
    --SessionId 1111 2222
```

Output: 
```
{
    "Response": {
        "RequestId": "14f6980a-7fe1-11ea-b896-525400542aa6",
        "TaskId": 11
    }
}
```

