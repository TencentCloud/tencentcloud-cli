**Example 1: DescribeMNPDomainACL**



Input: 

```
tccli tcmpp DescribeMNPDomainACL --cli-unfold-argument  \
    --MNPId mpg9yjc0qbpkelik \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "DomainUrl": "https://console.tencent.com",
                "DomainType": 1
            },
            {
                "DomainUrl": "https://console.tencent.com",
                "DomainType": 2
            }
        ],
        "RequestId": "0400caf9-dc30-48f9-bb87-870c78a078b1"
    }
}
```

