**Example 1: 请求示例**



Input: 

```
tccli redis CloneInstances --cli-unfold-argument  \
    --AlarmPolicyList xx \
    --TemplateId xx \
    --VpcId xx \
    --InstanceId xx \
    --AutoRenew 1 \
    --SubnetId xx \
    --Password xx \
    --GoodsNum 1 \
    --ProjectId 0 \
    --ZoneId 1 \
    --ResourceTags.0.TagKey xx \
    --ResourceTags.0.TagValue xx \
    --VPort 1 \
    --InstanceName xx \
    --SecurityGroupIdList xx \
    --NodeSet.0.ZoneName xx \
    --NodeSet.0.NodeType 0 \
    --NodeSet.0.NodeId 0 \
    --NodeSet.0.ZoneId 1 \
    --Period 1 \
    --BillingMode 0 \
    --BackupId xx \
    --NoAuth True
```

Output: 
```
{
    "Response": {
        "RequestId": "2a836c00-175f-11eb-aeb3-db134c8d8fec",
        "InstanceIds": [
            "crs-kic39axx"
        ],
        "DealId": "22716"
    }
}
```

