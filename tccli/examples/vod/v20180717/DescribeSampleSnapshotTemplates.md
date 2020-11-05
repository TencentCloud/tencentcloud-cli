**Example 1: Querying the list of sampled screencapturing templates**



Input: 

```
tccli vod DescribeSampleSnapshotTemplates --cli-unfold-argument  \
    --Definitions 10001
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SampleSnapshotTemplateSet": [
            {
                "Definition": 10001,
                "Type": "Custom",
                "Name": "Sampled screencapturing template 1",
                "Comment": "",
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z",
                "Format": "jpg",
                "Height": 540,
                "SampleType": "Percent",
                "SampleInterval": 10,
                "Width": 960
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

