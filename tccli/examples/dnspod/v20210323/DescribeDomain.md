**Example 1: 获取域名信息**

 

Input: 

```
tccli dnspod DescribeDomain --cli-unfold-argument  \
    --Domain dnspod.cn
```

Output: 
```
{
    "Response": {
        "DomainInfo": {
            "ActualNsList": [],
            "CnameSpeedup": "disable",
            "CreatedOn": "2023-03-21 17:27:40",
            "DnsStatus": "dnserror",
            "DnspodNsList": [
                "temporary.dnspod.net",
                "barman.dnspod.net"
            ],
            "Domain": "dnspod.cn",
            "DomainId": 12620688,
            "Grade": "DP_FREE",
            "GradeLevel": 2,
            "GradeTitle": "免费版",
            "GroupId": 1,
            "IsGracePeriod": "no",
            "IsMark": "no",
            "IsSubDomain": false,
            "IsVip": "no",
            "Owner": "qcloud_uin_100000******@qcloud.com",
            "OwnerNick": "昵称",
            "Punycode": "dnspod.cn",
            "RecordCount": 182761,
            "Remark": "",
            "SearchEnginePush": "no",
            "SlaveDNS": "no",
            "Status": "enable",
            "TTL": 600,
            "TagList": [],
            "Uin": "100000******",
            "UpdatedOn": "2024-12-30 10:16:57",
            "UserId": 5301126,
            "VipAutoRenew": null,
            "VipBuffered": "no",
            "VipEndAt": null,
            "VipResourceId": null,
            "VipStartAt": null
        },
        "RequestId": "c1ea5ee3-aa4b-446e-a42d-859b9461487b"
    }
}
```

