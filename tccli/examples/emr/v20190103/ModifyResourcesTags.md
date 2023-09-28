**Example 1: test**



Input: 

```
tccli emr ModifyResourcesTags --cli-unfold-argument  \
    --ModifyType abc \
    --ModifyResourceTagsInfoList.0.ResourceId abc \
    --ModifyResourceTagsInfoList.0.Resource abc \
    --ModifyResourceTagsInfoList.0.ResourcePrefix abc \
    --ModifyResourceTagsInfoList.0.ResourceRegion abc \
    --ModifyResourceTagsInfoList.0.ServiceType abc \
    --ModifyResourceTagsInfoList.0.DeleteTags.0.TagKey abc \
    --ModifyResourceTagsInfoList.0.DeleteTags.0.TagValue abc \
    --ModifyResourceTagsInfoList.0.AddTags.0.TagKey abc \
    --ModifyResourceTagsInfoList.0.AddTags.0.TagValue abc \
    --ModifyResourceTagsInfoList.0.ModifyTags.0.TagKey abc \
    --ModifyResourceTagsInfoList.0.ModifyTags.0.TagValue abc
```

Output: 
```
{
    "Response": {
        "ClusterToFlowIdList": [
            {
                "ClusterId": "emr-2qhwmqln",
                "FlowId": 79
            }
        ],
        "SuccessList": [
            "abc"
        ],
        "FailList": [
            "abc"
        ],
        "PartSuccessList": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

