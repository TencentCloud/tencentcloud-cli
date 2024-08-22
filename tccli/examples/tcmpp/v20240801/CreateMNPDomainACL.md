**Example 1: CreateMNPDomainACL**



Input: 

```
tccli tcmpp CreateMNPDomainACL --cli-unfold-argument  \
    --MNPId mpg9yjc0qbpkelik \
    --Domain.0.DomainType 1 \
    --Domain.0.DomainUrlList https://console.tencent.com \
    --Domain.1.DomainType 2 \
    --Domain.1.DomainUrlList https://console.tencent.com \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "d9700b29-dd0d-4661-8ec1-f9e9b351139d"
    }
}
```

