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
                "DcnFlag": 1,
                "DcnStatus": 0,
                "InstanceId": "tdsql-2rn9lmpx",
                "InstanceName": "tdsql-2rn9lmpx",
                "Region": "ap-guangzhou",
                "Status": 2,
                "StatusDesc": "运行中",
                "Vip": "10.0.0.24",
                "Vipv6": "",
                "Vport": 3306,
                "Zone": "ap-guangzhou-4"
            },
            {
                "DcnFlag": 2,
                "DcnStatus": 2,
                "InstanceId": "tdsql-cbr0g5v1",
                "InstanceName": "tdsql-cbr0g5v1",
                "Region": "ap-guangzhou",
                "Status": 2,
                "StatusDesc": "运行中",
                "Vip": "10.0.0.29",
                "Vipv6": "",
                "Vport": 3306,
                "Zone": "ap-guangzhou-4"
            }
        ],
        "RequestId": "cbca1c8e-e123-11ea-a777-525400542aa6"
    }
}
```

