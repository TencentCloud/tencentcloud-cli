**Example 1: 导出下载恶意请求文件**

导出下载恶意请求文件

Input: 

```
tccli cwp ExportMaliciousRequests --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://cwp-1258344***.cos.ap-guangzhou.myqcloud.com/file.txt",
        "RequestId": "acdd5474-6360-4fd4-bfc7-843162cb8116",
        "TaskId": "1"
    }
}
```

