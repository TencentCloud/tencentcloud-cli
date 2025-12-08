**Example 1: 创建资源包绑定策略**

无

Input: 

```
tccli billing ModifyMeasurePackageBindStrategy --cli-unfold-argument  \
    --ProductCode p_snapshot \
    --BindProductCode p_snapshot \
    --Operations.0.Operate add \
    --Operations.0.BindSubProductCode sp_snapshot_normal \
    --Operations.0.ResourceId snap-j4d000ezWGZGU67 \
    --Operations.0.BindObjectId test-p_snapshot-12 \
    --Operations.0.RegionId 2 \
    --Operations.0.BindProperties.0.PropertyKey regionId \
    --Operations.0.BindProperties.0.PropertyValue 2 \
    --EventTime 2025-12-04 17:30:00
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": 0
        },
        "RequestId": "ce076ed0-3463-4344-a13d-5ce846854ff0"
    }
}
```

