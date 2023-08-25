**Example 1: 获取导出任务结果**

获取导出任务结果

Input: 

```
tccli dsgc DescribeExportTaskResult --cli-unfold-argument  \
    --DspaId dspa-xxx \
    --ExportTaskId 460
```

Output: 
```
{
    "Response": {
        "RequestId": "128009ac-7df4-0530-cc92-52f0d945e191",
        "ExportResult": "Success",
        "ExportFileUrl": "https://xxx"
    }
}
```

