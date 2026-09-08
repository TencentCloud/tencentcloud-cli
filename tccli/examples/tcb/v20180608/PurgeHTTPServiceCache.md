**Example 1: 清除EO缓存**



Input: 

```
tccli tcb PurgeHTTPServiceCache --cli-unfold-argument  \
    --EnvId **********-1gz1k5qkc06a0da4 \
    --Domain *********************.cn \
    --Targets https://*********************.cn/cloudbaseenv.json \
    --PurgeType PURGE_URL \
    --CacheType EO
```

Output: 
```
{
    "Response": {
        "CacheType": "EO",
        "TaskId": "3uk1onlg81ab",
        "RequestId": "f6f50b8b-6ada-42cb-9ae4-fa35d37c5cf0"
    }
}
```

