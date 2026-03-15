**Example 1: 创建视频主体**



Input: 

```
tccli vod CreateAigcSubject --cli-unfold-argument  \
    --SubAppId 221073 \
    --SubjectName mySessionName \
    --SubjectVideos *** \
    --SessionContext mySessionContext \
    --TasksPriority 10
```

Output: 
```
{
    "Response": {
        "TaskId": "221073-CreateAigcSubject-f9aa5a12**********cdd403de6fcd07t",
        "RequestId": "e78603c5-2fd1-417a-91f5-023728963868"
    }
}
```

