**Example 1: 列出预热任务信息**



Input: 

```
tccli goosefs ListLoadTasks --cli-unfold-argument  \
    --ClusterId g_cvm_hlg97c61 \
    --Offset 0 \
    --Limit 1 \
    --StartTimestamp 1767859318 \
    --EndTimestamp 1767859328
```

Output: 
```
{
    "Response": {
        "LoadTaskList": [],
        "TotalCount": 0,
        "RequestId": "3a0256cf-ddb6-4273-ae44-205a007707ed"
    }
}
```

