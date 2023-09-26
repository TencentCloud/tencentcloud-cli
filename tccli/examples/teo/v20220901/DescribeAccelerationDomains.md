**Example 1: 查询指定站点下的域名信息**

查询指定 zone-id 的下的源站类型为 IP_DOMAIN 的所有加速域名的信息，并将结果按照创建时间降序排列。

Input: 

```
tccli teo DescribeAccelerationDomains --cli-unfold-argument  \
    --ZoneId zone-20hyebgyfsko \
    --Filters.0.Fuzzy True \
    --Filters.0.Values IP_DOMAIN \
    --Filters.0.Name origin-type \
    --Direction desc \
    --Order created_on \
    --Match all
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AccelerationDomains": [
            {
                "ZoneId": "zone-20hyebgyfsko",
                "DomainName": "www.qq.com",
                "DomainStatus": "online",
                "OriginDetail": {
                    "OriginType": "IP_DOMAIN",
                    "Origin": "origin.qq.com",
                    "BackupOrigin": "",
                    "PrivateParameters": [],
                    "PrivateAccess": "",
                    "OriginGroupName": "",
                    "BackOriginGroupName": ""
                },
                "IdentificationStatus": "finished",
                "Cname": "www.qq.com.eo.dnse3.com",
                "CreatedOn": "2020-09-22T00:00:00+00:00",
                "ModifiedOn": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "5e5a0d0f-52f3-4bad-9bd3-dcf1d5c954e7"
    }
}
```

