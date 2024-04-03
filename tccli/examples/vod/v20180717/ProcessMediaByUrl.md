**Example 1: 发起内容分析任务**

对 URL 为 ```http://www.abc.com/abc.mp4``` 的视频发起内容分析任务。

Input: 

```
tccli vod ProcessMediaByUrl --cli-unfold-argument  \
    --InputInfo.Url http://www.abc.com/abc.mp4 \
    --InputInfo.Name 大国外交 \
    --InputInfo.Id 872988202 \
    --OutputInfo.Region ap-guangzhou \
    --OutputInfo.Bucket myoutputbucket-1256244234 \
    --OutputInfo.Dir /output/test/ \
    --AiAnalysisTask.Definition 10
```

Output: 
```
{
    "Response": {
        "RequestId": "5ca61e3a-6b8e-4b4e-9256-fdc701190064ef0",
        "TaskId": "125xxxxxx07-procedurev2-813dc41e6fdc22dcf24aa6e9c61cp92"
    }
}
```

**Example 2: 发起内容审核任务**

对 URL 为 ```http://www.abc.com/abc.mp4``` 的视频发起内容审核任务。

Input: 

```
tccli vod ProcessMediaByUrl --cli-unfold-argument  \
    --InputInfo.Url http://www.abc.com/abc.mp4 \
    --InputInfo.Name 大国外交 \
    --InputInfo.Id 872988202 \
    --OutputInfo.Region ap-guangzhou \
    --OutputInfo.Bucket myoutputbucket-1256244234 \
    --OutputInfo.Dir /output/test/ \
    --AiContentReviewTask.Definition 10
```

Output: 
```
{
    "Response": {
        "RequestId": "5ca61e3a-6b8e-4b4e-9256-fdc701190064ef0",
        "TaskId": "125xxxxxx07-procedurev2-893dc41e6fdc22dcf24aa6e9c61cp94"
    }
}
```

**Example 3: 发起内容识别任务**

对 URL 为 ```http://www.abc.com/abc.mp4``` 的视频发起内容识别任务。

Input: 

```
tccli vod ProcessMediaByUrl --cli-unfold-argument  \
    --InputInfo.Url http://www.abc.com/abc.mp4 \
    --InputInfo.Name 大国外交 \
    --InputInfo.Id 872988202 \
    --OutputInfo.Region ap-guangzhou \
    --OutputInfo.Bucket myoutputbucket-1256244234 \
    --OutputInfo.Dir /output/test/ \
    --AiRecognitionTask.Definition 10
```

Output: 
```
{
    "Response": {
        "RequestId": "5ca61e3a-6b8e-4b4e-9256-fdc701190064fk3",
        "TaskId": "125xxxxxx07-procedurev2-813dc41e6fdc22dcf24aa6e9c61f3t0"
    }
}
```

