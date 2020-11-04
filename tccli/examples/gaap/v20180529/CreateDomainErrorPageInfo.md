**Example 1: CreateDomainErrorPageInfo**



Input: 

```
tccli gaap CreateDomainErrorPageInfo --cli-unfold-argument  \
    --ListenerId 0\
    --Domain a.com\
    --ErrorNos 501 502\
    --NewErrorNo 400\
    --Body helloword
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8",
        "ErrorPageId": "errorPage-1fewf"
    }
}
```

