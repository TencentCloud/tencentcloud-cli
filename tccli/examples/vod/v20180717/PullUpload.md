**Example 1: Pulling an MP4 video from the ```http://www.abc.com/abc.mp4``` URL for upload**



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

**Example 2: Pulling an MP4 video from the ```http://www.abc.com/abc.mp4``` URL in Mainland China and uploading it to the Chongqing region**



Input: 

```
tccli vod PullUpload --cli-unfold-argument  \
    --MediaUrl http://www.abc.com/abc.mp4 \
    --StorageRegion ap-chongqing
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

**Example 3: Pulling an MP4 video from the ```http://www.abc.com/abc.mp4``` URL outside Mainland China and uploading it to the Singapore region**



Input: 

```
tccli vod PullUpload --cli-unfold-argument  \
    --MediaUrl http://www.abc.com/abc.mp4 \
    --StorageRegion ap-singapore
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

