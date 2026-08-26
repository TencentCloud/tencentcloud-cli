**Example 1: 查询模板列表**



Input: 

```
tccli cfw DescribeAddressTemplateList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Detail": "",
                "IPNum": 1,
                "InsertTime": "2026-08-21 11:08:24",
                "IpString": "*domai.com",
                "IpVersion": 0,
                "Name": "1121212",
                "ProtocolType": "",
                "RulesNum": 1,
                "TemplateId": "dm-d7zc5d4i",
                "Type": 5,
                "UpdateTime": "2026-08-21 11:08:24",
                "Uuid": "mb_1300448058_1787281704076"
            }
        ],
        "DomainTemplateCount": 3,
        "IpTemplateCount": 2,
        "NameList": [
            "tke模板"
        ],
        "PortTemplateCount": 2,
        "TemplateQuotaCount": 10,
        "TkeTemplateCount": 0,
        "Total": 7,
        "UsedTemplateCount": 9,
        "RequestId": "1030842f-ad26-414d-9b7d-bde6dc24c765"
    }
}
```

