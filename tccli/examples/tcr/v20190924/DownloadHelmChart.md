**Example 1: 下载Helm Chart**



Input: 

```
tccli tcr DownloadHelmChart --cli-unfold-argument  \
    --RegistryId tcr-xxx \
    --NamespaceName tcr-test \
    --ChartName test \
    --ChartVersion 1.0
```

Output: 
```
{
    "Response": {
        "TmpToken": "XXXX",
        "TmpSecretId": "XXXX",
        "TmpSecretKey": "XXXX",
        "Bucket": "XXXX",
        "Region": "XXXX",
        "Path": "tcr-test/test-1.0.tgz",
        "StartTime": "12345",
        "ExpiredTime": "123456",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

