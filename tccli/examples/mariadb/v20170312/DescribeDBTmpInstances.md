**Example 1: 无**



Input: 

```
tccli mariadb DescribeDBTmpInstances --cli-unfold-argument  \
    --InstanceId xx
```

Output: 
```
{
    "Response": {
        "TmpInstances": [
            {
                "Status": 0,
                "SrcInstanceId": "xx",
                "Zone": "xx",
                "InstanceId": "xx",
                "Region": "xx",
                "TempType": 0,
                "InstanceRemark": "xx",
                "Vip": "xx",
                "AppId": 0,
                "PeriodEndTime": "2020-09-22 00:00:00",
                "Ipv6Flag": 1,
                "Vport": 0,
                "StatusDesc": "xx",
                "Vipv6": "xx",
                "CreateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "xx"
    }
}
```

