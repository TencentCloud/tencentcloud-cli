**Example 1: 成功**

成功调用上传

Input: 

```
tccli aiart UploadTrainPortraitImages --cli-unfold-argument  \
    --ModelId test \
    --BaseUrl https://xxx.com/xxx.jpg \
    --Urls https://xxx.com/yyy.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "948182a1-e669-42f8-a00e-fa9f5b7d287a",
        "ResultDetails": [
            "SUCCESS"
        ]
    }
}
```

