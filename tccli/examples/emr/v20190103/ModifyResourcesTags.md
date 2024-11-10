**Example 1: test**



Input: 

```
tccli emr ModifyResourcesTags --cli-unfold-argument  \
    --ModifyResourceTagsInfoList.0.ModifyTags.0.TagKey tke-zzy \
    --ModifyResourceTagsInfoList.0.ModifyTags.0.TagValue master \
    --ModifyResourceTagsInfoList.0.Resource qcs::emr:ap-guangzhou:uin/51000000:emr-vm/emr-vm-bnm \
    --ModifyResourceTagsInfoList.0.ResourceId emr-vm-bnm \
    --ModifyResourceTagsInfoList.0.ResourcePrefix emr-vm \
    --ModifyResourceTagsInfoList.0.ResourceRegion ap-guangzhou \
    --ModifyResourceTagsInfoList.0.ServiceType emr \
    --ModifyType Node
```

Output: 
```
{
    "Response": {
        "ClusterToFlowIdList": [
            {
                "ClusterId": "emr-mir",
                "FlowId": 1834233
            }
        ],
        "FailList": null,
        "PartSuccessList": null,
        "RequestId": "eee79a8e-0714-4406-9973-bf4084899a87",
        "SuccessList": null
    }
}
```

