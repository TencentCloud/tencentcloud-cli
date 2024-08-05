**Example 1: demo**

demo

Input: 

```
tccli tcmpp CheckGlobalDomain --cli-unfold-argument  \
    --DomainUrlList abc \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": {
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

