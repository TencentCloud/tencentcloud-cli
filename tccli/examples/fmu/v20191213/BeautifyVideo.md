**Example 1: 调用返回成功**



Input: 

```
tccli fmu BeautifyVideo --cli-unfold-argument  \
    --Url 字符串 \
    --OutputVideoType 字符串 \
    --BeautyParam.0.WhitenLevel 整型 \
    --BeautyParam.0.SmoothingLevel 整型 \
    --BeautyParam.0.EyeEnlargeLevel 整型 \
    --BeautyParam.0.FaceShrinkLevel 整型
```

Output: 
```
{
    "Response": {
        "JobId": "Vi6QGs7jO3uylsZY",
        "EstimatedProcessTime": 30,
        "RequestId": "327cd4c8-e544-43db-ba0c-3afda873ac73"
    }
}
```

