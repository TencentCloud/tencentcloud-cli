**Example 1: 获取视频重生模板列表。**

获取视频重生模板列表。

Input: 

```
tccli vod DescribeRebuildMediaTemplates --cli-unfold-argument  \
    --Definitions 20001
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RebuildMediaTemplateSet": [
            {
                "Definition": 20001,
                "Name": "template name",
                "Type": "Preset",
                "Comment": "",
                "RebuildVideoInfo": null,
                "RebuildAudioInfo": null,
                "TargetVideoInfo": null,
                "TargetAudioInfo": null,
                "Container": "mp4",
                "RemoveVideo": 0,
                "RemoveAudio": 0,
                "CreateTime": "",
                "UpdateTime": ""
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

