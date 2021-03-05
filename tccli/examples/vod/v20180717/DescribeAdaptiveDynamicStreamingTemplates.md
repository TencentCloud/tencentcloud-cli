**Example 1: 查询转自适应码流模板列表**



Input: 

```
tccli vod DescribeAdaptiveDynamicStreamingTemplates --cli-unfold-argument  \
    --Definitions 10001
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AdaptiveDynamicStreamingTemplateSet": [
            {
                "Definition": 1001,
                "Type": "Custom",
                "Name": "转自适应码流模板1",
                "Comment": "",
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z",
                "DrmType": "",
                "DisableHigherVideoBitrate": 1,
                "DisableHigherVideoResolution": 0
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

