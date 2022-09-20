**Example 1: 查询域名证书列表**



Input: 

```
tccli teo DescribeHostCertificates --cli-unfold-argument  \
    --Sort.Key create_time \
    --Sort.Sequence desc \
    --Limit 100 \
    --Filters.0.Fuzzy True \
    --Filters.0.Values zone-dfascdsf \
    --Filters.0.Name zone-id \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "HostCertificates": [
            {
                "Host": "www.test,com",
                "HostCertInfo": [
                    {
                        "CertId": "cert-dfadsfa",
                        "Type": "default",
                        "Status": "process",
                        "Alias": "www.tencent.com",
                        "ExpireTime": "2014-08-03T12:00:00+08:00",
                        "DeployTime": "2014-08-03T12:00:00+08:00",
                        "SignAlgo": "RSA 2048"
                    }
                ]
            }
        ],
        "RequestId": "xxxx-xxxx-xxxx"
    }
}
```

