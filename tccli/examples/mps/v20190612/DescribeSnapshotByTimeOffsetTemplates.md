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
        "TotalCount": 1,
        "SnapshotByTimeOffsetTemplateSet": [
            {
                "Definition": 1,
                "Type": "abc",
                "Name": "abc",
                "Comment": "abc",
                "Width": 1,
                "Height": 1,
                "ResolutionAdaptive": "abc",
                "Format": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "FillType": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

