**Example 1: 直播课回放下载**

该API获取直播课回放下载地址

Input: 

```
tccli tcop DescribeFastReplayDownloads --cli-unfold-argument  \
    --IdaasOrgId tn-c65190017f394836863e83ca429b500c \
    --VId 1000030510
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://ke.qq.com/1",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

