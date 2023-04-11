**Example 1: 请求示例**

克隆实例

Input: 

```
tccli redis CloneInstances --cli-unfold-argument  \
    --InstanceId abc \
    --GoodsNum 1 \
    --NoAuth True \
    --VpcId abc \
    --SubnetId abc \
    --ZoneId 1 \
    --InstanceName abc \
    --BillingMode 0 \
    --Period 1 \
    --Password abc \
    --AutoRenew 1 \
    --SecurityGroupIdList abc \
    --VPort 1 \
    --BackupId abc \
    --NodeSet.0.NodeId 0 \
    --NodeSet.0.NodeType 0 \
    --NodeSet.0.ZoneId 1 \
    --NodeSet.0.ZoneName abc \
    --ProjectId 0 \
    --ResourceTags.0.TagKey abc \
    --ResourceTags.0.TagValue abc \
    --TemplateId abc \
    --AlarmPolicyList abc
```

Output: 
```
{
    "Response": {
        "RequestId": "2a836c00-175f-11eb-aeb3-db134c8d8fec",
        "InstanceIds": [
            "crs-kic3****"
        ],
        "DealId": "22716"
    }
}
```

