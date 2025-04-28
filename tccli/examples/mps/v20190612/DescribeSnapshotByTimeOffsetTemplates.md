**Example 1: 获取指定时间点截图模板列表**



Input: 

```
tccli mps DescribeSnapshotByTimeOffsetTemplates --cli-unfold-argument  \
    --Definitions 10001
```

Output: 
```
{
    "Response": {
        "RequestId": "5c3410ca-abcd-467f-8014-0bfb6538ad73",
        "SnapshotByTimeOffsetTemplateSet": [
            {
                "Comment": "时间点截图模板test1",
                "CreateTime": "2017-10-26T10:36:51Z",
                "Definition": 10,
                "FillType": "stretch",
                "Format": "jpg",
                "Height": 0,
                "Name": "10时间点截图模版",
                "ResolutionAdaptive": "open",
                "Type": "Preset",
                "UpdateTime": "2019-07-25T22:22:55Z",
                "Width": 0
            }
        ],
        "TotalCount": 1
    }
}
```

