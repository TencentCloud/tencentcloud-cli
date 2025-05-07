**Example 1: 成功**

成功调用上传

Input: 

```
tccli aiart UploadTrainPortraitImages --cli-unfold-argument  \
    --ModelId model_01 \
    --BaseUrl https://xxx.com/image.jpg \
    --TrainMode 1
```

Output: 
```
{
    "Response": {
        "RequestId": "948182a1-e669-42f8-a00e-fa9f5b7d287a",
        "ResultDetails": []
    }
}
```

