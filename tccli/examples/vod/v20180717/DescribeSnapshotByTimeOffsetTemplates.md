**Example 1: 获取指定时间点截图模板列表**



Input: 

```
tccli vod DescribeSnapshotByTimeOffsetTemplates --cli-unfold-argument  \
    --Definitions 10001
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SnapshotByTimeOffsetTemplateSet": [
            {
                "Definition": 10001,
                "Type": "Custom",
                "Name": "指定时间点截图模板1",
                "Comment": "",
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z",
                "ResolutionAdaptive": "open",
                "FillType": "black",
                "Format": "jpg",
                "Height": 540,
                "Width": 960
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

