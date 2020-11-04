**Example 1: 图像质量评估请求成功**



Input: 

```
tccli tiia AssessQuality --cli-unfold-argument  \
    --ImageUrl https://test.jpg
```

Output: 
```
{
    "Response": {
        "LongImage": false,
        "BlackAndWhite": false,
        "SmallImage": false,
        "BigImage": true,
        "PureImage": false,
        "ClarityScore": 93,
        "AestheticScore": 92,
        "RequestId": "bfd478e1-5c94-4e37-ad22-4a5224a09492"
    }
}
```

