**Example 1: 无**



Input: 

```
tccli dcdb DescribeDBInstanceRsip --cli-unfold-argument  \
    --InstanceId dcdbt-21dfpcv1
```

Output: 
```
{
    "Response": {
        "RequestId": "69f16b01-ca70-4097-9acf-7e7a20d79424",
        "Rsips": [
            {
                "Ip": "100.100.34.245",
                "Port": 24113
            },
            {
                "Ip": "100.100.36.142",
                "Port": 24113
            },
            {
                "Ip": "100.100.34.245",
                "Port": 24114
            },
            {
                "Ip": "100.100.36.142",
                "Port": 24114
            }
        ]
    }
}
```

