**Example 1: 无**



Input: 

```
tccli mariadb DescribeDBInstanceRsip --cli-unfold-argument  \
    --InstanceId tdsql-lyzax5rb
```

Output: 
```
{
    "Response": {
        "RequestId": "d140c889-4cee-474c-8e6c-94ad52b9670c",
        "Rsips": [
            {
                "Ip": "100.98.175.239",
                "Port": 24414
            },
            {
                "Ip": "100.98.183.235",
                "Port": 24414
            }
        ]
    }
}
```

