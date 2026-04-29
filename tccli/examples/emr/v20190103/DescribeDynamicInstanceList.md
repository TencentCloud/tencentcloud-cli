**Example 1: DynamicInstance列表**



Input: 

```
tccli emr DescribeDynamicInstanceList --cli-unfold-argument  \
    --InstanceId emr-a2jqs6n3
```

Output: 
```
{
    "Response": {
        "DynamicInstanceList": [
            {
                "CreateTime": "2025-12-27 16:43:18",
                "PodCount": 4,
                "RayClusterId": 28,
                "RayClusterName": "raycluster",
                "RedisCount": 1,
                "SubmitType": 1
            },
            {
                "CreateTime": "2025-12-27 14:58:55",
                "PodCount": 2,
                "RayClusterId": 26,
                "RayClusterName": "raycluster-template",
                "RedisCount": 0,
                "SubmitType": 2
            },
            {
                "CreateTime": "2025-12-29 10:00:14",
                "PodCount": 2,
                "RayClusterId": 31,
                "RayClusterName": "raycluster-template111",
                "RedisCount": 0,
                "SubmitType": 2
            },
            {
                "CreateTime": "2025-12-25 09:56:44",
                "PodCount": 2,
                "RayClusterId": 14,
                "RayClusterName": "rayclusterb",
                "RedisCount": 0,
                "SubmitType": 1
            }
        ],
        "RequestId": "232ecc58-b00a-429c-8d6d-e399cd40c6cc"
    }
}
```

