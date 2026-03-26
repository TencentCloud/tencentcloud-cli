**Example 1: 获取部署服务cos信息**



Input: 

```
tccli tcb DescribeBuildServiceCosInfo --cli-unfold-argument  \
    --EnvId gangweiran-wushan-4euixce65321c0 \
    --Business static-hosting \
    --ServiceName kong111 \
    --UnixTimestamp  \
    --Suffix .zip \
    --NeedDownload False
```

Output: 
```
{
    "Response": {
        "DownloadHeaders": [],
        "DownloadUrl": "",
        "RequestId": "DescribeBuildServiceCosInfo-kong-222",
        "UnixTimestamp": "1763105497",
        "UploadHeaders": [],
        "UploadUrl": "https://abc.com/home/c0e39"
    }
}
```

