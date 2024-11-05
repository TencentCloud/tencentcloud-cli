**Example 1: 查询本地镜像组件列表导出**



Input: 

```
tccli tcss CreateVulExportJob --cli-unfold-argument  \
    --ImageID sha256:80beff5ff34259ceb7fbe9cd10b2d94912618f5b5595f234349c5bb0cd4f9211 \
    --Limit 10 \
    --Offset 0 \
    --ExportField CVEID
```

Output: 
```
{
    "Response": {
        "RequestId": "d1b9dbe2-f78d-491a-b514-f0aa19d8ae4b",
        "JobId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe"
    }
}
```

