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
        "RequestId": "xx",
        "JobId": "xx"
    }
}
```

