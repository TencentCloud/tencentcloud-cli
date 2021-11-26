**Example 1: 在项目中导入云点播文件**



Input: 

```
tccli cme ImportMediaToProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId cmepid_6f16967b64436100015fb046 \
    --SourceType VOD \
    --VodFileId 52858908114334690679 \
    --Name 视频1 \
    --PreProcessDefinition 10
```

Output: 
```
{
    "Response": {
        "MaterialId": "248208104522663991",
        "TaskId": "125xxx65-procedurev2-bffb15f07530b57bc1aabb01fac74bca",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e56"
    }
}
```

**Example 2: 在项目中导入外部媒体**

在项目中导入一个外部链接。

Input: 

```
tccli cme ImportMediaToProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId cmepid_6f16967b64436100015fb046 \
    --SourceType EXTERNAL \
    --Name 视频2 \
    --ExternalMediaInfo.Definition 1000000 \
    --ExternalMediaInfo.MediaKey 1810000000.vod2.myqcloud.com/b64e98acvodcq1810000000/f69747475285890810007930755/f0.mp4 \
    --PreProcessDefinition 10
```

Output: 
```
{
    "Response": {
        "MaterialId": "248208104522663991",
        "TaskId": "125xxxxxx65-procedurev2-3ab512f07530b88bc1aabb01fac345bcd",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e738"
    }
}
```

