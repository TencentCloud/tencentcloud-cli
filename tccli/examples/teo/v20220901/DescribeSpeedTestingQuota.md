**Example 1: 查询站点配额**

查询站点配额

Input: 

```
tccli teo DescribeSpeedTestingQuota --cli-unfold-argument  \
    --ZoneId zone-fiandfa
```

Output: 
```
{
    "Response": {
        "RequestId": "f9a45aa8-01ab-40c0-ac2d-e61178fd2c51",
        "SpeedTestingQuota": {
            "AvailableTestRuns": 0,
            "TotalTestRuns": 100
        }
    }
}
```

