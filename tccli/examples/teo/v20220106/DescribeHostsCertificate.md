**Example 1: 查询域名证书列表**



Input: 

```
tccli teo DescribeHostsCertificate --cli-unfold-argument  \
    --ZoneId xx \
    --Limit 100 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Hosts": [
            {
                "Host": "www.test,com",
                "CertInfo": [
                    {
                        "CertId": "xxxx",
                        "Type": "default",
                        "Alias": "xxxx",
                        "ExpireTime": "2014-08-03T12:00:00+08:00",
                        "DeployTime": "2014-08-03T12:00:00+08:00"
                    }
                ]
            }
        ],
        "RequestId": "xxxx-xxxx-xxxx"
    }
}
```

