**Example 1: 回滚快照**

 

Input: 

```
tccli dnspod RollbackSnapshot --cli-unfold-argument  \
    --Domain domain.com \
    --SnapshotId A45XXX33
```

Output: 
```
{
    "Response": {
        "RequestId": "42aabd52-d05b-45f0-95a0-dcefdc87c7b8",
        "TaskId": 177
    }
}
```

