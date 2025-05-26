**Example 1: 创建资源包绑定策略**

无

Input: 

```
tccli billing CreateMeasurePackageBindStrategy --cli-unfold-argument  \
    --ProductCode p_snapshot \
    --BindProductCode p_snapshot \
    --ResourceIds snap-j4d000ezWGZGU67 \
    --BindObjectId test-p_snapshot \
    --RegionId 1 \
    --BindProperties.0.PropertyKey regionId \
    --BindProperties.0.PropertyValue 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": 0
        },
        "RequestId": "e9d12c06-ea7f-400c-97e1-3b1b88522639"
    }
}
```

