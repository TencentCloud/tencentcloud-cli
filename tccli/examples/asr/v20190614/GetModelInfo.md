**Example 1: 通过模型id获取模型信息**

通过模型id获取模型信息

Input: 

```
tccli asr GetModelInfo --cli-unfold-argument  \
    --ModelId 5a15aa3ae4c611eda0d56c92bf48cdf2
```

Output: 
```
{
    "Response": {
        "Data": {
            "ModelName": "test",
            "DictName": "c6824a6d-05ec-431c-95c9",
            "ModelId": "5a15aa3ae4c611eda0d56c92bf48cdf2",
            "ModelType": "8k",
            "ServiceType": "",
            "ModelState": 1,
            "AtUpdated": "2023-04-27 14:40:09",
            "TagInfos": null
        },
        "RequestId": "abc"
    }
}
```

