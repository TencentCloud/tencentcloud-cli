**Example 1: 获取直播录制模板**

获取直播录制模板

Input: 

```
tccli mps DescribeLiveRecordTemplates --cli-unfold-argument  \
    --Definitions 20001
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LiveRecordTemplateSet": [
            {
                "Definition": 20001,
                "HLSConfigure": {
                    "ItemDuration": 10,
                    "Interval": 3600
                },
                "Name": "模板1",
                "Comment": "",
                "Type": "Preset",
                "CreateTime": "2023-05-04T10:00:00Z",
                "UpdateTime": "2023-05-04T10:00:00Z"
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

