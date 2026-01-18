**Example 1: CreateDomainErrorPageInfo**



Input: 

```
tccli gaap CreateDomainErrorPageInfo --cli-unfold-argument  \
    --ListenerId listener-oh6gsmzh \
    --Domain winsons.site \
    --ErrorNos 403 \
    --Body http-body \
    --NewErrorNo 400
```

Output: 
```
{
    "Response": {
        "ErrorPageId": "errorPage-qkmqxjxx",
        "RequestId": "30f43d0d-7c4e-492f-8de0-803ed7722426"
    }
}
```

