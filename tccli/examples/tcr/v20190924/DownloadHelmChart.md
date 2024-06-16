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
        "TmpSecretKey": "abc",
        "TmpToken": "abc",
        "Region": "ap-guangzhou",
        "Bucket": "tcr-d3av5-536254",
        "TmpSecretId": "abc",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "StartTime": 0,
        "Path": "/docker/registry",
        "ExpiredTime": 0
    }
}
```

