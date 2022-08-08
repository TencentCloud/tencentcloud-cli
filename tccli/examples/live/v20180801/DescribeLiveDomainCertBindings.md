**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveDomainCertBindings --cli-unfold-argument  \
    --DomainSearch  \
    --DomainName abc.com \
    --Offset 0 \
    --Length 50
```

Output: 
```
{
    "Response": {
        "RequestId": "3b4a072b-9f74-4baa-9200-1e0858baa7a5",
        "LiveDomainCertBindings": [],
        "TotalNum": 0
    }
}
```

