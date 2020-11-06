**Example 1: 请求示例**



Input: 

```
tccli redis DescribeInstanceShards --cli-unfold-argument  \
    --InstanceId crs-7ponppu3
```

Output: 
```
{
    "Response": {
        "InstanceShards": [
            {
                "Keys": 0,
                "Role": 0,
                "ShardId": "1",
                "ShardName": "crs-7ponppu3-003-01",
                "Slots": "[\"0-5460\"]",
                "Storage": 3096688,
                "StorageSlope": -0.002399486489594
            },
            {
                "Keys": 0,
                "Role": 1,
                "ShardId": "1",
                "ShardName": "crs-7ponppu3-003-02",
                "Slots": "[]",
                "Storage": 3035608,
                "StorageSlope": 0
            },
            {
                "Keys": 0,
                "Role": 0,
                "ShardId": "2",
                "ShardName": "crs-7ponppu3-001-01",
                "Slots": "[\"5461-10922\"]",
                "Storage": 3160280,
                "StorageSlope": 0.018086727708578
            },
            {
                "Keys": 0,
                "Role": 1,
                "ShardId": "2",
                "ShardName": "crs-7ponppu3-001-02",
                "Slots": "[]",
                "Storage": 3036632,
                "StorageSlope": 0
            },
            {
                "Keys": 0,
                "Role": 0,
                "ShardId": "3",
                "ShardName": "crs-7ponppu3-002-01",
                "Slots": "[\"10923-16383\"]",
                "Storage": 3055440,
                "StorageSlope": -0.015687562525272
            },
            {
                "Keys": 0,
                "Role": 1,
                "ShardId": "3",
                "ShardName": "crs-7ponppu3-002-02",
                "Slots": "[]",
                "Storage": 3035608,
                "StorageSlope": 0
            }
        ],
        "RequestId": "ca3000b6-bb8a-41fd-9074-11b5fda52d9f"
    }
}
```

