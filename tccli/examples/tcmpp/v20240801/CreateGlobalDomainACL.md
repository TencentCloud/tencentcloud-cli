**Example 1: CreateGlobalDomainACL**



Input: 

```
tccli tcmpp CreateGlobalDomainACL --cli-unfold-argument  \
    --DomainType 1 \
    --DomainUrlList openapi.autotest.domain.com \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true,
            "RepeatUrls": [],
            "ExistsWhiteUrls": [],
            "ExistsBlackUrls": []
        },
        "RequestId": "aaf521b9-f1f7-4167-896c-c9a276f34ea7"
    }
}
```

