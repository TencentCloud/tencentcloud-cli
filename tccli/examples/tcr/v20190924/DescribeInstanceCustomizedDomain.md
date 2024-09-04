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
        "RequestId": "12445-5556-11",
        "DomainInfoList": [
            {
                "Status": "success",
                "CertId": "14568-152",
                "RegistryId": "tcr-12345",
                "DomainName": "tcr.test"
            }
        ],
        "TotalCount": 10
    }
}
```

