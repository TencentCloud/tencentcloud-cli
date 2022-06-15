**Example 1: DDos攻击TopN数据**



Input: 

```
tccli teo DescribeDDosAttackTopData --cli-unfold-argument  \
    --AttackType xx \
    --MetricName xx \
    --ProtocolType xx \
    --PolicyIds 0 \
    --ZoneIds xx \
    --Limit 0 \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --Port 0
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Msg": "success",
        "Data": [
            {
                "Value": [
                    {
                        "Count": 123,
                        "Name": "udp"
                    }
                ],
                "Key": "subzoneId2"
            }
        ],
        "RequestId": "xx"
    }
}
```

