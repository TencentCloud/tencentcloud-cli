**Example 1: 创建复杂自适应码流任务**

将一个媒体文件（带有视频和中文音频）转码并打包为自适应码流，同时额外添加片头、英文音频、中文字幕和英文字幕。
主媒体的 FileId 为4424135347909043783，且设置 Chinese 和 English 两个字幕；与主媒体匹配的英文音频的 FileId 为4424135347909043652；自适应码流模板为220368；片头模板为14591。

Input: 

```
tccli vod CreateComplexAdaptiveDynamicStreamingTask --cli-unfold-argument  \
    --SubAppId 1250000000 \
    --FileId 4424135347909043783 \
    --StreamParaSet.0.Definition 220368 \
    --HeadTailSet.0.Definition 14591 \
    --AudioSet.0.FileId 4424135347909043783 \
    --AudioSet.0.Name Chinese \
    --AudioSet.0.Language zh \
    --AudioSet.0.Default YES \
    --AudioSet.1.FileId 4424135347909043652 \
    --AudioSet.1.Name English \
    --AudioSet.1.Language en \
    --SubtitleSet.0.Id Chinese \
    --SubtitleSet.0.Default YES \
    --SubtitleSet.1.Id English
```

Output: 
```
{
    "Response": {
        "RequestId": "2e1af3fa-a55f-4078-9d61-df448c1e6e34",
        "TaskId": "1250000000-ComplexAdaptiveDynamicStreaming-a9e3993dd4fdee822862cd80c43ac4c4t"
    }
}
```

