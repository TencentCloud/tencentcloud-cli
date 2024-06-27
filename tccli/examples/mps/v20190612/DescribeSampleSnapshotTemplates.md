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
                "Definition": 1,
                "Type": "abc",
                "Name": "abc",
                "Comment": "abc",
                "Width": 1,
                "Height": 1,
                "ResolutionAdaptive": "abc",
                "Format": "abc",
                "SampleType": "abc",
                "SampleInterval": 1,
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "FillType": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

