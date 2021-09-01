**Example 1: 生成应用程序包预签名下载链接**

生成应用程序包预签名下载链接

Input: 

```
tccli tem GenerateApplicationPackageDownloadUrl --cli-unfold-argument  \
    --PkgName xx \
    --DeployVersion xx \
    --ApplicationId xx \
    --SourceChannel 0
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

