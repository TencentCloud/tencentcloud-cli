**Example 1: CreatePositionFence**

创建围栏

Input: 

```
tccli iotexplorer CreatePositionFence --cli-unfold-argument  \
    --SpaceId 5bf5407370cc40848f39a2896a2ab052 \
    --FenceName TestFence \
    --FenceDesc TT \
    --FenceArea {"type":"FeatureCollection","features":[{"type":"Feature","geometry":{"type":"Polygon","coordinates":[[[113.9498,22.5319],[113.9709,22.5319],[113.9709,22.5723],[113.9498,22.5723],[113.9498,22.5319]]]},"properties":null}]}
```

Output: 
```
{
    "Response": {
        "RequestId": "1e99faaf-a0f0-4c49-9d85-7f09f2b7f74e"
    }
}
```

