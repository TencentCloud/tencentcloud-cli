**Example 1: 包分类余量预警**



Input: 

```
tccli billing DescribeMeasureResourceAlarmThreshold --cli-unfold-argument  \
    --ProductCode p_cdn \
    --ThresholdType 4 \
    --GroupId cdn_flux_aa
```

Output: 
```
{
    "Response": {
        "Data": {
            "ThresholdValueType": 0,
            "Thresholds": [
                5,
                20,
                30
            ],
            "ProductCode": "p_cdn",
            "ResourceId": "",
            "Uin": "700000860361",
            "GroupId": "cdn_flux_aa",
            "ThresholdType": 4
        },
        "RequestId": "abc"
    }
}
```

