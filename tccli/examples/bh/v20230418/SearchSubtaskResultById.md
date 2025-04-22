**Example 1: 查询运维子任务执行结果**

查询运维子任务执行结果

Input: 

```
tccli bh SearchSubtaskResultById --cli-unfold-argument  \
    --Status 1 \
    --Name 运维任务 \
    --Limit 1 \
    --Id west \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082"
    }
}
```

