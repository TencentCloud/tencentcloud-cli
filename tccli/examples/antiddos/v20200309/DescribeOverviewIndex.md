**Example 1: 拉取防护概览指标**



Input: 

```
tccli antiddos DescribeOverviewIndex --cli-unfold-argument  \
    --StartTime '2020-02-01 12:04:12' \
    --EndTime '2020-02-03 18:03:23'
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "AllIpCount": 100,
        "AntiddosIpCount": 10,
        "AttackIpCount": 2,
        "BlockIpCount": 1,
        "AntiddosDomainCount": 10,
        "AttackDomainCount": 2,
        "MaxAttackFlow": 245,
        "NewAttackTime": "2021-05-15 21:43:15",
        "NewAttackIp": "10.34.14.54",
        "NewAttackType": "SYNFLOOD"
    }
}
```

