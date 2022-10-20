**Example 1: 查询木马自动隔离样本下载链接**



Input: 

```
tccli tcss DescribeVirusAutoIsolateSampleDownloadURL --cli-unfold-argument  \
    --MD5 dskaldjskld
```

Output: 
```
{
    "Response": {
        "FileUrl": "xx",
        "RequestId": "xx"
    }
}
```

