**Example 1: 查询本地镜像组件列表导出**



Input: 

```
tccli tcss CreateComponentExportJob --cli-unfold-argument  \
    --ImageID xx \
    --Limit 10 \
    --Offset 0 \
    --ExportField xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "JobId": "xx"
    }
}
```

