**Example 1: 创建受漏洞影响的容器导出任务**



Input: 

```
tccli tcss CreateVulContainerExportJob --cli-unfold-argument  \
    --PocID 1
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

