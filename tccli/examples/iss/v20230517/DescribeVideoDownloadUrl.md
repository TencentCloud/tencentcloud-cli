**Example 1: 获取云录像下载URL**

 

Input: 

```
tccli iss DescribeVideoDownloadUrl --cli-unfold-argument  \
    --ChannelId 4dfb778c-xxxxxx \
    --BeginTime 1668996000 \
    --EndTime 1668996600 \
    --FileType mp4
```

Output: 
```
{
    "Response": {
        "Data": {
            "Url": "https://userdomain/video.mp4?source=xxxxxx",
            "ActualBeginTime": "1668996000",
            "ActualEndTime": "1668996600"
        },
        "RequestId": "******************"
    }
}
```

**Example 2: 获取云录像下载URL和实际下载的录像时间**

指定请求参数IsRespActualTime为true， 不指定或IsRespActualTime为false时，不返回实际的时间

Input: 

```
tccli iss DescribeVideoDownloadUrl --cli-unfold-argument  \
    --ChannelId 4dfb778c-xxxxxxx \
    --BeginTime 1668996000 \
    --EndTime 1668996600 \
    --FileType mp4 \
    --IsRespActualTime True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Url": "https://userdomain/video.mp4?source=xxxxxx",
            "ActualBeginTime": "1668996000",
            "ActualEndTime": "1668996600"
        },
        "RequestId": "******************"
    }
}
```

