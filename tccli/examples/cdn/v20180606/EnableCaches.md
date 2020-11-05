**Example 1: Unblocking a URL**



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
        }
    }
}
```

