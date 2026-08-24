**Example 1: DescribeCkafkaRouteList**



Input: 

```
tccli csip DescribeDspmCkafkaRouteList --cli-unfold-argument  \
    --VipType 0 \
    --RegionId ap-guangzhou \
    --InstanceId ins-woinsla \
    --InstanceName ins-2wqsasad
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Vip": "vpc-2wqsa",
                "Vport": "3006",
                "Domain": "www.mysql.com",
                "DomainPort": "80"
            }
        ],
        "TotalCount": 1,
        "RequestId": "24adbdda-a605-4501-9e8c-3f0894936a62"
    }
}
```

