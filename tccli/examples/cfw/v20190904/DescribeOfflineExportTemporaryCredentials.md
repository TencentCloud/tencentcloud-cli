**Example 1: 获取日志离线导出任务文件下载临时凭证**

获取日志离线导出任务文件下载临时凭证

Input: 

```
tccli cfw DescribeOfflineExportTemporaryCredentials --cli-unfold-argument  \
    --TaskId 99281
```

Output: 
```
{
    "Response": {
        "RequestId": "2d8786ee-788f-440a-84bd-cd191f6cc18d",
        "ReturnCode": 0,
        "ReturnMsg": "success"
    }
}
```

