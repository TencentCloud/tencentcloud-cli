**Example 1: demo**

demo

Input: 

```
tccli tcmpp CreateGlobalDomain --cli-unfold-argument  \
    --DomainUrlList abc \
    --DomainType 0 \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true,
            "RepeatUrls": [
                "abc"
            ],
            "ExistsWhiteUrls": [
                "abc"
            ],
            "ExistsBlackUrls": [
                "abc"
            ]
        },
        "RequestId": "abc"
    }
}
```

