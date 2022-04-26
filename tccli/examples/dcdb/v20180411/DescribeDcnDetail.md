**Example 1: 无**



Input: 

```
tccli dcdb DescribeDcnDetail --cli-unfold-argument  \
    --InstanceId tdsql-2rn9lmpx
```

Output: 
```
{
    "Response": {
        "DcnDetails": [
            {
                "Status": 2,
                "DcnStatus": 0,
                "DcnFlag": 1,
                "Zone": "ap-guangzhou-4",
                "InstanceId": "tdsql-2rn9lmpx",
                "InstanceName": "tdsdql-2rn9lmpx",
                "Region": "ap-guangzhou",
                "Storage": 0,
                "InstanceType": 0,
                "Cpu": 0,
                "PayMode": 0,
                "Vip": "10.0.0.24",
                "Memory": 0,
                "PeriodEndTime": "2019-02-01 10:00:00",
                "Vport": 3306,
                "StatusDesc": "运行中",
                "Vipv6": "",
                "CreateTime": "2019-01-01 10:00:00"
            },
            {
                "Status": 2,
                "DcnStatus": 2,
                "DcnFlag": 2,
                "Zone": "xx",
                "InstanceId": "tdsql-cbr0g5v1",
                "Vipv6": "",
                "Region": "ap-guangzhou",
                "Storage": 0,
                "Cpu": 0,
                "PayMode": 0,
                "Vip": "10.0.0.25",
                "CreateTime": "2019-01-01 10:00:00",
                "Memory": 0,
                "PeriodEndTime": "2019-02-01 10:00:00",
                "Vport": 3306,
                "StatusDesc": "运行中",
                "InstanceName": "tdsql-cbr0g5v1",
                "InstanceType": 0
            }
        ],
        "RequestId": "cbca1c8e-e123-11ea-a777-525400542aa6"
    }
}
```

