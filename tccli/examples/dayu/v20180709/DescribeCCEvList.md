**Example 1: 获取CC攻击事件列表**



Input: 

```
tccli dayu DescribeCCEvList --cli-unfold-argument  \
    --Business bgp \
    --Id bgp-00000010 \
    --IpList 3.3.3.3 \
    --StartTime '2018-08-27 15:05:10' \
    --EndTime '2018-08-27 16:05:10' \
    --Limit 30 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Business": "bgp",
        "Data": [
            {
                "Business": "bgp",
                "Id": "bgp-00000010",
                "Vip": "3.3.3.3",
                "StartTime": "2018-08-27 15:05:10",
                "EndTime": "2018-08-27 16:05:10",
                "ReqQps": 544231,
                "DropQps": 13232,
                "AttackStatus": 1,
                "DomainList": "www.dw.com;www.ksd.com",
                "UriList": "/sef/sdf;/tesf/sdf",
                "AttackipList": "1.1.1.1;2.2.3.2"
            }
        ],
        "EndTime": "2019-03-07 14:50:00",
        "Id": "bgp-00000010",
        "IpList": [
            "3.3.3.3"
        ],
        "RequestId": "69b1692b-4b6e-47c0-a7d6-0ff0da286874",
        "StartTime": "2019-03-07 00:00:00",
        "Total": 1
    }
}
```

