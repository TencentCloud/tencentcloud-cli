**Example 1: 删除媒体文件**

视频文件不需要保存，删除该FileId下全部文件和信息。

Input: 

```
tccli vod DeleteMedia --cli-unfold-argument  \
    --FileId 7447398156998994860 \
    --SubAppId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "requestId"
    }
}
```

**Example 2: 删除部分转码视频**

只想删除部分defination的转码视频，保留其他格式的转码视频。
例如删除转码defination为230的HLS文件，并且同时删除HLS Master Playlist

Input: 

```
tccli vod DeleteMedia --cli-unfold-argument  \
    --FileId 7447398156998994860 \
    --SubAppId 1 \
    --DeleteParts.0.Type TranscodeFiles \
    --DeleteParts.0.Definition 230 \
    --DeleteParts.1.Type TranscodeFiles \
    --DeleteParts.1.Definition 10000
```

Output: 
```
{
    "Response": {
        "RequestId": "requestId"
    }
}
```

**Example 3: 删除转码视频和微信发布视频**

删除指定FileId下的全部转码文件及微信发布文件。
保留源文件，保留转码和截图等其他任务流生成的文件和信息。

Input: 

```
tccli vod DeleteMedia --cli-unfold-argument  \
    --FileId 7447398156998994860 \
    --SubAppId 1 \
    --DeleteParts.0.Type TranscodeFiles \
    --DeleteParts.1.Type WechatPublishFiles
```

Output: 
```
{
    "Response": {
        "RequestId": "requestId"
    }
}
```

