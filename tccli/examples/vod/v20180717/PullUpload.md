**Example 1: 拉取上传一个 URL 为 ```http://www.abc.com/abc.mp4``` 的 MP4 视频。**

拉取上传 MP4 视频

Input: 

```
tccli vod PullUpload --cli-unfold-argument  \
    --MediaUrl http://www.abc.com/abc.mp4
```

Output: 
```
{
    "Response": {
        "RequestId": "5ca61e3a-6b8e-4b4e-9256-fdc701190064ef0",
        "TaskId": "125xxxxxx07-pull-893dc41e6fdc22dcf24aa6e9c61cp94"
    }
}
```

**Example 2: 拉取上传一个国内 URL 为 ```http://www.abc.com/abc.mp4``` 的 MP4 视频至重庆园区。**

拉取上传 MP4 视频至重庆园区

Input: 

```
tccli vod PullUpload --cli-unfold-argument  \
    --StorageRegion ap-chongqing \
    --MediaUrl http://www.abc.com/abc.mp4
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca61e3a-6b8e-4b4e-9256-fdc701190064ef0",
        "TaskId": "125xxxxxx07-pull-793dc41e6fdc22dcf24aa6e9c61cp94"
    }
}
```

**Example 3: 拉取上传一个海外 URL 为 ```http://www.abc.com/abc.mp4``` 的 MP4 视频至新加坡园区。**

拉取上传 MP4 至新加坡园区

Input: 

```
tccli vod PullUpload --cli-unfold-argument  \
    --StorageRegion ap-singapore \
    --MediaUrl http://www.abc.com/abc.mp4
```

Output: 
```
{
    "Response": {
        "RequestId": "5ca61e3a-6b8e-4b4e-9256-fdc701190064ef0",
        "TaskId": "125xxxxxx07-pull-693dc41e6fdc22dcf24aa6e9c61cp94"
    }
}
```

