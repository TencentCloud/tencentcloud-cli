**Example 1: Getting DDoS protection usage statistics**



Input: 

```
tccli dayu DescribeDDoSUsedStatis --cli-unfold-argument  \
    --Business bgpip
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Key": "Days",
                "Value": "365"
            },
            {
                "Key": "Attacks",
                "Value": "30"
            }
        ],
        "RequestId": "8f7a9451-2372-4a88-a69d-9868b8991076"
    }
}
```

