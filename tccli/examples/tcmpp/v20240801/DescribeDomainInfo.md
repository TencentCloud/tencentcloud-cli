**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeDomainInfo --cli-unfold-argument  \
    --MNPId abc \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "DomainUrl": "abc",
                "DomainType": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

