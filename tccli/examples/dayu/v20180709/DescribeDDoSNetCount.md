**Example 1: Getting DDoS attack proportion analysis for Anti-DDoS Ultimate resource**



Input: 

```
tccli dayu DescribeDDoSNetCount --cli-unfold-argument  \
    --Business net \
    --Id net-00000010 \
    --StartTime '2018-08-27 15:05:10' \
    --EndTime '2018-08-27 16:05:10' \
    --MetricName pkg
```

Output: 
```
{
    "Response": {
        "Business": "net",
        "Data": [],
        "EndTime": "2019-03-07 14:50:00",
        "Id": "net-000000y0",
        "RequestId": "69b1692b-4b6e-47c0-a7d6-0ff0da286874",
        "StartTime": "2019-03-07 00:00:00"
    }
}
```

