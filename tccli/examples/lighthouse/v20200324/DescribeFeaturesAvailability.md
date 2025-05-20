**Example 1: 查询创建实例是否支持IPv6**

查询当前资源组合是否支持在创建实例后自动开启IPv6。

Input: 

```
tccli lighthouse DescribeFeaturesAvailability --cli-unfold-argument  \
    --Features.0.FeatureDimensions.0.Name BlueprintId \
    --Features.0.FeatureDimensions.0.Values lhbp-8l0svqtk \
    --Features.0.FeatureDimensions.1.Name BundleId \
    --Features.0.FeatureDimensions.1.Values bundle_starter_mc_med2_01 \
    --Features.0.FeatureDimensions.2.Name InstanceCount \
    --Features.0.FeatureDimensions.2.Values 10 \
    --Features.0.FeatureDimensions.3.Name Zone \
    --Features.0.FeatureDimensions.3.Values ap-guangzhou-2 \
    --Features.0.FeatureName CREATE_INSTANCE_SUPPORT_IPV6
```

Output: 
```
{
    "Response": {
        "FeatureAvailabilityResults": [
            {
                "FeatureName": "CREATE_INSTANCE_SUPPORT_IPV6",
                "IsAvailable": true,
                "Message": "支持分配IPv6。"
            }
        ],
        "RequestId": "90c1b3d3-8cc3-49f6-b81c-e70c8e3f9308"
    }
}
```

