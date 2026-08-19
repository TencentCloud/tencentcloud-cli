**Example 1: 查询腾讯云SCF自定义域名端点列表**



Input: 

```
tccli csip DescribeScfCustomDomainEndpoints --cli-unfold-argument  \
    --AssetID lwj-ap*01.liuc****an.com \
    --MemberId mem-68b80*7a65**8000
```

Output: 
```
{
    "Response": {
        "Endpoints": [
            {
                "FunctionName": "http-django-*6*Z6*a2Zx",
                "Namespace": "default",
                "PathMatch": "/*",
                "Qualifier": "$DEFAULT"
            }
        ],
        "RequestId": "3aecfb59-bb07-48b8-b57b-589c6be8ec70"
    }
}
```

