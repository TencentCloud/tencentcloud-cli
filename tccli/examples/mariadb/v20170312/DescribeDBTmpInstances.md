**Example 1: 无**



Input: 

```
tccli mariadb DescribeDBTmpInstances --cli-unfold-argument  \
    --InstanceId tdsql-oc5srykh
```

Output: 
```
{
    "Response": {
        "TmpInstances": [
            {
                "Status": 2,
                "SrcInstanceId": "tdsql-ow728lmc",
                "Zone": "ap-guangzhou-3",
                "InstanceId": "tdsql-oc5srykh",
                "Region": "ap-guangzhou",
                "TempType": 0,
                "InstanceRemark": "临时实例",
                "Vip": "10.0.0.30",
                "AppId": 251202055,
                "PeriodEndTime": "2020-09-22 00:00:00",
                "Ipv6Flag": 1,
                "Vport": 0,
                "StatusDesc": "运行中",
                "Vipv6": "",
                "CreateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "35e66783-c90f-46e2-aeac-758d51133094"
    }
}
```

