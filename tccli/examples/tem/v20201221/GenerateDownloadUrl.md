**Example 1: 生成包预签名下载链接**

生成包预签名下载链接

Input: 

```
tccli tem GenerateDownloadUrl --cli-unfold-argument  \
    --SourceChannel 0 \
    --DeployVersion xx \
    --ServiceId xx \
    --PkgName xx
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": {}
    }
}
```

