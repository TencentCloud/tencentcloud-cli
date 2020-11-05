**Example 1: Querying AZs in a specified region**



Input: 

```
tccli postgres DescribeZones --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "59c438d4-95ab-4865-993d-dc388d2660d8",
        "TotalCount": 3,
        "ZoneSet": [
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "Guangzhou Zone 2",
                "ZoneId": 100002,
                "ZoneState": "AVAILABLE"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "Guangzhou Zone 3",
                "ZoneId": 100003,
                "ZoneState": "AVAILABLE"
            },
            {
                "Zone": "ap-guangzhou-4",
                "ZoneName": "Guangzhou Zone 4",
                "ZoneId": 100004,
                "ZoneState": "AVAILABLE"
            }
        ]
    }
}
```

