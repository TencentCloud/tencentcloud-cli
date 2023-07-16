**Example 1: 调用返回成功**

调用返回成功

Input: 

```
tccli fmu BeautifyVideo --cli-unfold-argument  \
    --Url abc \
    --BeautyParam.0.WhitenLevel 1 \
    --BeautyParam.0.SmoothingLevel 1 \
    --BeautyParam.0.EyeEnlargeLevel 1 \
    --BeautyParam.0.FaceShrinkLevel 1 \
    --OutputVideoType abc
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

