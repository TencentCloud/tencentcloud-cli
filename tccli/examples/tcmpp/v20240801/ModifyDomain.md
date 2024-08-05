**Example 1: demo**

demo

Input: 

```
tccli tcmpp ModifyDomain --cli-unfold-argument  \
    --MNPId abc \
    --PlatformId abc \
    --Domain.0.DomainUrlList abc \
    --Domain.0.DomainType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "abc"
    }
}
```

