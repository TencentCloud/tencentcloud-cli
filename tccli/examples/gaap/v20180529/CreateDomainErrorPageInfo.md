**Example 1: CreateDomainErrorPageInfo**



Input: 

```
tccli gaap CreateDomainErrorPageInfo --cli-unfold-argument  \
    --Body http-body \
    --Domain domain.com \
    --ListenerId 0 \
    --ErrorNos 502 501 \
    --NewErrorNo 400
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

