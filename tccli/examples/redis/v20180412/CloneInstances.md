**Example 1: 示例**



Input: 

```
tccli redis CloneInstances --cli-unfold-argument  \
    --InstanceId crs-qbhudciv \
    --GoodsNum 1 \
    --ZoneId 10002 \
    --BillingMode 0 \
    --Period 1 \
    --SecurityGroupIdList sg-bmadczm1 \
    --BackupId 154572601-1165734322-153705740 \
    --VpcId vpc-bmadczcc \
    --SubnetId subnet-bmadczcc
```

Output: 
```
{
    "Response": {
        "DealId": "20250825297021530591847",
        "DealName": "20260407296022526727811",
        "InstanceIds": [
            "crs-lqz7y86j"
        ],
        "RequestId": "b841398d-94ea-42a1-ac2c-663853bcf5f9"
    }
}
```

