**Example 1: 导出核心文件事件**

导出核心文件事件

Input: 

```
tccli cwp ExportFileTamperEvents --cli-unfold-argument  \
    --Filters.0.Values 0 \
    --Filters.0.Name Level \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TaskId": "1596595610"
    }
}
```

