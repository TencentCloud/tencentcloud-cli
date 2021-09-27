**Example 1: 解封示例**



Input: 

```
tccli cdn EnableCaches --cli-unfold-argument  \
    --Urls http://example.com/path/to.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "asdasdascsa721d8ha8chsa",
        "CacheOptResult": {
            "FailUrls": [],
            "SuccessUrls": [
                "http://example.com/path/to.jpg"
            ]
        },
        "TaskId": "1632627566746100176"
    }
}
```

