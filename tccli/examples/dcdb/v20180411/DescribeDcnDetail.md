**Example 1: 获取实例灾备详情**

获取实例灾备详情

Input: 

```
tccli dcdb DescribeDcnDetail --cli-unfold-argument  \
    --InstanceId tdsqlshard-hqtjy5d1
```

Output: 
```
{
    "Response": {
        "DcnDetails": [
            {
                "Cpu": 0,
                "CreateTime": "2022-11-08 17:43:48",
                "DcnFlag": 1,
                "DcnStatus": 0,
                "EncryptStatus": 0,
                "InstanceId": "tdsqlshard-hqtjy5d1",
                "InstanceName": "tdsqlshard-hqtjy5d1",
                "InstanceType": 2,
                "Memory": 0,
                "PayMode": 0,
                "PeriodEndTime": "0001-01-01 00:00:00",
                "Region": "ap-guangzhou",
                "Status": 2,
                "StatusDesc": "运行中",
                "Storage": 0,
                "Vip": "172.16.16.86",
                "Vipv6": "",
                "Vport": 3306,
                "Zone": "ap-guangzhou-3"
            },
            {
                "Cpu": 0,
                "CreateTime": "2022-11-08 17:56:43",
                "DcnFlag": 2,
                "DcnStatus": 2,
                "EncryptStatus": 0,
                "InstanceId": "tdsqlshard-c06stiq3",
                "InstanceName": "tdsqlshard-c06stiq3",
                "InstanceType": 3,
                "Memory": 0,
                "PayMode": 0,
                "PeriodEndTime": "0001-01-01 00:00:00",
                "Region": "ap-guangzhou",
                "Status": 2,
                "StatusDesc": "运行中",
                "Storage": 0,
                "Vip": "172.16.16.18",
                "Vipv6": "",
                "Vport": 3306,
                "Zone": "ap-guangzhou-3"
            }
        ],
        "RequestId": "f1989672-5114-4289-a0b5-3b5b4c11dccc"
    }
}
```

