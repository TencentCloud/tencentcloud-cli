**Example 1: ModifyMNPDomain**



Input: 

```
tccli tcmpp ModifyMNPDomain --cli-unfold-argument  \
    --MNPId mpg9yjc0qbpkelik \
    --Domain.0.DomainType 2 \
    --Domain.1.DomainType 3 \
    --Domain.2.DomainType 4 \
    --Domain.3.DomainType 5 \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "7a78d408-060a-4fc6-8f21-d937d8caedf6"
    }
}
```

