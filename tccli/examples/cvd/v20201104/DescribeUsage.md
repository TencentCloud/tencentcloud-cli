**Example 1: DescribeUsage**



Input: 

```
tccli cvd DescribeUsage --cli-unfold-argument  \
    --PageSize 20 \
    --PageNumber 1 \
    --StartTime 1735660800 \
    --EndTime 1735747200
```

Output: 
```
{
    "Response": {
        "UsageSet": [
            {
                "InstanceId": "cdi-sd8dhw8osu0jcw6",
                "Name": "test-cvd",
                "Status": "RUNNING",
                "UserName": "test-user",
                "ChargeType": "PREPAID",
                "InstanceType": "S1L.LARGE8",
                "OsName": "Windows Server 2019",
                "ActiveTime": "00:20:20",
                "IdleTime": "00:01:00"
            }
        ],
        "Total": 1,
        "QueryKey": "d298-4c88-b7ff-0eabf528d566",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

