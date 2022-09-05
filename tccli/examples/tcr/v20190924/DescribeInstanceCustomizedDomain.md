**Example 1: 查询实例自定义域名列表**



Input: 

```
tccli tcr DescribeInstanceCustomizedDomain --cli-unfold-argument  \
    --RegistryId tcr-12345 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "DomainInfoList": [
            {
                "Status": "xx",
                "CertId": "xx",
                "RegistryId": "xx",
                "DomainName": "xx"
            }
        ],
        "TotalCount": 10
    }
}
```

