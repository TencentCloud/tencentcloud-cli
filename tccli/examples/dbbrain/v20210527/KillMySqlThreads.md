**Example 1: 根据会话ID中断当前会话**

Stage为"commit"阶段

Input: 

```
tccli dbbrain KillMySqlThreads --cli-unfold-argument  \
    --InstanceId cdb-8jawylhf \
    --SqlExecId 2e2e2 \
    --Stage Commit \
    --Product mysql
```

Output: 
```
{
    "Response": {
        "SqlExecId": "ewfscd",
        "Threads": [
            0
        ],
        "RequestId": "sscrft"
    }
}
```

