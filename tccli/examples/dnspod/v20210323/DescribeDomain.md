**Example 1: 获取域名信息**

 

Input: 

```
tccli dnspod DescribeDomain --cli-unfold-argument  \
    --Domain dnspod.com
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "DomainInfo": {
            "DnspodNsList": [
                "source.dnspod.net",
                "low.dnspod.net"
            ],
            "ActualNsList": [
                "f1g1ns1.dnspod.net",
                "f1g1ns2.dnspod.net"
            ],
            "RecordCount": 2,
            "DomainId": 61,
            "DnsStatus": "dnserror",
            "IsVip": "no",
            "Punycode": "tencent8.com",
            "Grade": "DP_FREE",
            "GradeLevel": 2,
            "GradeTitle": "免费版",
            "Status": "enable",
            "GroupId": 1,
            "IsMark": "no",
            "Remark": "",
            "UserId": 1,
            "CreatedOn": "2021-04-06 15:51:45",
            "UpdatedOn": "2021-04-06 15:51:45",
            "TTL": 600,
            "Owner": "qcloud_uin_100000014226@qcloud.com",
            "CnameSpeedup": "disable",
            "Uin": "100000014226",
            "OwnerNick": "Loccsser",
            "Domain": "tencent8.com"
        }
    }
}
```

