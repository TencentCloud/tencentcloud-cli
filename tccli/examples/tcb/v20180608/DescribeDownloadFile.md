**Example 1: 获取文件下载信息**

获取文件下载信息

Input: 

```
tccli tcb DescribeDownloadFile --cli-unfold-argument  \
    --CodeUri extension://ba883a90xxxxx.zip
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://cloudaccess-code-123.cos.ap-shanghai.myqcloud.com/aaa",
        "CustomKey": "xxx",
        "FilePath": "file",
        "RequestId": "d691f154-c2d5-4f48-833a-a408cdaadd9c"
    }
}
```

