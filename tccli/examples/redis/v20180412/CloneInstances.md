**Example 1: 请求示例**

克隆实例

Input: 

```
tccli redis CloneInstances --cli-unfold-argument  \
    --InstanceId crs-qddzg*** \
    --GoodsNum 1 \
    --ZoneId 200005 \
    --BillingMode 0 \
    --Period 1 \
    --SecurityGroupIdList sg-o0lb0*** \
    --BackupId 331006369-11071477-******* \
    --VpcId vpc-c9v9o*** \
    --SubnetId subnet-7054l*** \
    --InstanceName InstanceName-redis-preversion \
    --Password pwd********** \
    --NodeSet.0.NodeType 0 \
    --NodeSet.0.ZoneName ap-shanghai-5 \
    --NodeSet.1.NodeType 1 \
    --NodeSet.1.ZoneName ap-shanghai-2 \
    --ProjectId 1 \
    --ResourceTags.0.TagKey key1 \
    --ResourceTags.0.TagValue value2 \
    --AlarmPolicyList policy-r7529***
```

Output: 
```
{
    "Response": {
        "RequestId": "2a836c00-175f-11eb-aeb3-db134c8dXXXX",
        "InstanceIds": [
            "crs-kic3****"
        ],
        "DealName": "20250825297021530591847"
    }
}
```

