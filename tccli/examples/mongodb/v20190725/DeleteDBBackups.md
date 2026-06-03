**Example 1: 删除全量备份**

删除全量备份

Input: 

```
tccli mongodb DeleteDBBackups --cli-unfold-argument  \
    --InstanceId cmgo-51l0dj35 \
    --BackupIds 39983
```

Output: 
```
{
    "Response": {
        "RequestId": "9ab09c94-b2fc-4053-9115-ccc178e56000"
    }
}
```

