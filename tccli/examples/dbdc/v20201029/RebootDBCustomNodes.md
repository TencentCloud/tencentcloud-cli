**Example 1: 重启 DB Custom 节点**



Input: 

```
tccli dbdc RebootDBCustomNodes --cli-unfold-argument  \
    --NodeIds dbcn-679g2lfs \
    --StopType SOFT_FIRST
```

Output: 
```
{
    "Response": {
        "TaskId": 491,
        "RequestId": "5a598d1b-5e7c-4fe7-b07c-f7599cdf8a07"
    }
}
```

