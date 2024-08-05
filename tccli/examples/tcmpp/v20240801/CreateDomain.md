**Example 1: demo**

demo

Input: 

```
tccli tcmpp CreateDomain --cli-unfold-argument  \
    --MNPId abc \
    --Domain.0.DomainUrlList abc \
    --Domain.0.DomainType 0 \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": 0,
        "RequestId": "abc"
    }
}
```

