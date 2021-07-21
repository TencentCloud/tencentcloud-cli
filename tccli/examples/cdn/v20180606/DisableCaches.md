**Example 1: 封禁示例**



Input: 

```
tccli cdn DisableCaches --cli-unfold-argument  \
    --Urls http://example.com/path/to.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "f13cf55b-69e6-4937-8856-bd8965beea8c",
        "CacheOptResult": {
            "SuccessUrls": [
                "http://example.com/path/to.jpg"
            ],
            "FailUrls": []
        },
        "TaskId": "xx"
    }
}
```

