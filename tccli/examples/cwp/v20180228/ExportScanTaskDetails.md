**Example 1: 导出扫描任务详情**

导出扫描任务详情

Input: 

```
tccli cwp ExportScanTaskDetails --cli-unfold-argument  \
    --ModuleType abc \
    --TaskId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TaskId": "1615549629"
    }
}
```

