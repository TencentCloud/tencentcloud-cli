**Example 1: 创建分散置放群组**

创建分散置放群组

Input: 

```
tccli cvm CreateDisasterRecoverGroup --cli-unfold-argument  \
    --Name MySWDisasterRecoverGroup \
    --Type SW \
    --Affinity 3 \
    --TagSpecification.0.ResourceType ps \
    --TagSpecification.0.Tags.0.Key MySWDisasterRecoverGroupKey \
    --TagSpecification.0.Tags.0.Value MySWDisasterRecoverGroupValue
```

Output: 
```
{
    "Response": {
        "CreateTime": "2025-11-17 07:43:06",
        "CurrentNum": 0,
        "CvmQuotaTotal": 20,
        "DisasterRecoverGroupId": "ps-39lmgkht",
        "Name": "MySWDisasterRecoverGroup",
        "RequestId": "59216e4c-c24d-46f8-bc88-ebc5081a595f",
        "Type": "SW"
    }
}
```

