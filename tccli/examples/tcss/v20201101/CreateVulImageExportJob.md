**Example 1: 创建受漏洞影响的镜像导出任务**



Input: 

```
tccli tcss CreateVulImageExportJob --cli-unfold-argument  \
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

