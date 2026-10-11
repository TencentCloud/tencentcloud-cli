**Example 1: 查询采样截图模板列表**



Input: 

```
tccli mps DescribeSampleSnapshotTemplates --cli-unfold-argument  \
    --Definitions 10001
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SampleSnapshotTemplateSet": [
            {
                "Definition": 10,
                "Type": "Preset",
                "Name": "采样截图模板",
                "Comment": "采样截图模板说明",
                "Width": 0,
                "Height": 0,
                "ResolutionAdaptive": "open",
                "Format": "jpg",
                "SampleType": "Percent",
                "SampleInterval": 10,
                "CreateTime": "2017-10-26T18:34:44Z",
                "UpdateTime": "2017-10-26T18:34:44Z",
                "FillType": "stretch"
            }
        ],
        "RequestId": "008xxxxx-xxxx-xxxx-xxxx-xxxxxxxxaa48"
    }
}
```

