**Example 1: 获取扫描报告下载链接**



Input: 

```
tccli advisor DescribeDownloadTask --cli-unfold-argument  \
    --ResultId -1#Group#0f7c2fac-20ee-4da9-8e71-944577bf7616
```

Output: 
```
{
    "Response": {
        "CosUrl": "xx",
        "CosUrlPdf": "xx",
        "RequestId": "xx",
        "TaskStatus": "xx"
    }
}
```

