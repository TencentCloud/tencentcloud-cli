**Example 1: 查询自学习模型列表**

查询自学习模型列表

Input: 

```
tccli asr GetCustomizationList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "5f44d72be3a308c9b62158b0",
        "TotalCount": 2,
        "Data": [
            {
                "ModelName": "dd",
                "DictName": "example.txt",
                "ModelId": "a07acb16e60311ea9a76b49691037310",
                "ModelType": "8k",
                "ServiceType": "realtime",
                "ModelState": -1,
                "AtUpdated": "2020-08-24 20:16:25",
                "TagInfos": null
            },
            {
                "ModelName": "ddd",
                "DictName": "example.txt",
                "ModelId": "98bda0fee60311ea9a76b49691037310",
                "ModelType": "16k",
                "ServiceType": "realtime",
                "ModelState": -1,
                "AtUpdated": "2020-08-24 20:16:15",
                "TagInfos": null
            }
        ]
    }
}
```

