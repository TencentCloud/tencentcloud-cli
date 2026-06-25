**Example 1: 异步获取 AIGC 人脸信息**



Input: 

```
tccli vod DescribeAigcFaceInfoAsync --cli-unfold-argument  \
    --SubAppId 250000002 \
    --FileInfos.0.Type Url \
    --FileInfos.0.Url https://150******************************************************************************************20.mp4 \
    --SessionId my*******Id1 \
    --SessionContext my*******Context \
    --TasksPriority 1
```

Output: 
```
{
    "Response": {
        "TaskId": "251007502-DescribeAigcFaceInfoAsync-d5a02998082d0a58cecd7e69165b5245t",
        "RequestId": "fc945039-2d72-4591-9ce7-780856bc4e24"
    }
}
```

