**Example 1: 查询地址模板列表**



Input: 

```
tccli cfw DescribeAddressTemplateList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --SearchValue 出向白名单 \
    --TemplateType 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Detail": "放通出方向目的ip",
                "IPNum": 4,
                "InsertTime": "2024-02-21 16:33:11",
                "IpString": "10.222.0.0/16,10.222.0.14,10.26.26.11,10.115.1.12",
                "IpVersion": 0,
                "Name": "出向白名单",
                "ProtocolType": "4",
                "RulesNum": 5,
                "TemplateId": "ip-863papye",
                "Type": 1,
                "UpdateTime": "2024-09-11 10:14:42",
                "Uuid": "mb_appid_1708504391199"
            }
        ],
        "DomainTemplateCount": 0,
        "IpTemplateCount": 1,
        "NameList": [
            "dora"
        ],
        "PortTemplateCount": 0,
        "RequestId": "f68d4fbb-4887-4fbb-91cb-e964131d5b4c",
        "TemplateQuotaCount": 300,
        "Total": 1,
        "UsedTemplateCount": 1
    }
}
```

