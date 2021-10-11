**Example 1: 获取围栏列表**



Input: 

```
tccli iotexplorer DescribePositionFenceList --cli-unfold-argument  \
    --SpaceId 5bf5407370cc40848f39a2896a2ab052 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "GeoFence": {
                    "FenceId": 6,
                    "SpaceId": "5bf5407370cc40848f39a2896a2ab052",
                    "FenceName": "TestFence",
                    "FenceDesc": "TT",
                    "FenceArea": "{\"type\":\"FeatureCollection\",\"features\":[{\"type\":\"Feature\",\"geometry\":{\"type\":\"Polygon\",\"coordinates\":[[[113.9498,22.5319],[113.9709,22.5319],[113.9709,22.5723],[113.9498,22.5723],[113.9498,22.5319]]]},\"properties\":null}]}"
                },
                "CreateTime": 1604030296579,
                "UpdateTime": 1604030296579
            },
            {
                "GeoFence": {
                    "FenceId": 17,
                    "SpaceId": "5bf5407370cc40848f39a2896a2ab052",
                    "FenceName": "TestFence1116",
                    "FenceDesc": "1116",
                    "FenceArea": "{\"type\":\"FeatureCollection\",\"features\":[{\"type\":\"Feature\",\"geometry\":{\"type\":\"Polygon\",\"coordinates\":[[[113.9498,22.5319],[113.9709,22.5319],[113.9709,22.5723],[113.9498,22.5723],[113.9498,22.5319]]]},\"properties\":null}]}"
                },
                "CreateTime": 1605510338840,
                "UpdateTime": 1605510338840
            },
            {
                "GeoFence": {
                    "FenceId": 38,
                    "SpaceId": "5bf5407370cc40848f39a2896a2ab052",
                    "FenceName": "TestFence1117",
                    "FenceDesc": "1117",
                    "FenceArea": "{\"type\":\"FeatureCollection\",\"features\":[{\"type\":\"Feature\",\"geometry\":{\"type\":\"Polygon\",\"coordinates\":[[[113.9498,22.5319],[113.9709,22.5319],[113.9709,22.5723],[113.9498,22.5723],[113.9498,22.5319]]]},\"properties\":null}]}"
                },
                "CreateTime": 1605584593250,
                "UpdateTime": 1605584593250
            }
        ],
        "RequestId": "f7b5e3e8-5089-4f11-b999-9a4c5952c4c5",
        "Total": 3
    }
}
```

