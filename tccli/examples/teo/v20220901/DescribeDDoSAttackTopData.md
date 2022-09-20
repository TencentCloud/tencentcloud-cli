**Example 1: DDoS攻击Top数据**



Input: 

```
tccli teo DescribeDDoSAttackTopData --cli-unfold-argument  \
    --AttackType UDPFLOOD \
    --MetricName ddos_attackFlux_protocol \
    --ProtocolType udp \
    --PolicyIds 1705 \
    --ZoneIds zone-21xfqlh4qjee \
    --Limit 1 \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --Port 22 \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "Data": [
            {
                "Value": [
                    {
                        "Count": 123,
                        "Name": "udp"
                    }
                ],
                "Key": "zone-21xfqlh4qjee"
            }
        ],
        "RequestId": "3824cf60-c2aa-4f4a-95b7-a4d5e4dee188"
    }
}
```

