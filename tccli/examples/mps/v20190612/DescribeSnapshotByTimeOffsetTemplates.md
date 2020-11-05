**Example 1: Getting the list of time point screencapturing templates**



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
                "Definition": 10001,
                "Type": "Custom",
                "Name": "Time point screencapturing template 1",
                "Comment": "",
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z",
                "Format": "jpg",
                "Height": 540,
                "Width": 960
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

