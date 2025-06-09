**Example 1: 分页查询已经注册过的声纹信息**



Input: 

```
tccli trtc DescribeVoicePrint --cli-unfold-argument  \
    --DescribeMode 1 \
    --PageIndex 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AppId": 1300056921,
                "AudioName": "jackson",
                "CreateTime": "2025-06-05 18:40:27",
                "ReqTimestamp": 1749119970000,
                "UpdateTime": "2025-06-05 18:40:27",
                "VoicePrintId": "20250605_e3f126cda7ad4196bfb1acfb10642d39fFPqPcCyY6KcccmO9t4CHqn-6qJMBnzaiLzdaeEi2Q",
                "VoicePrintMetaInfo": "custom_metainfo"
            }
        ],
        "RequestId": "10459f57-b3fb-42a3-99c7-0c037967e420",
        "TotalCount": 14
    }
}
```

