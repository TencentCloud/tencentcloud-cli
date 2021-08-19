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
                "StorageSlope": -0.002399486489594,
                "Runid": "af8945d6271e030ea17829b07c08e6c417bbff3d",
                "Connected": 1
            },
            {
                "Keys": 0,
                "Role": 1,
                "ShardId": "1",
                "ShardName": "crs-7ponppu3-003-02",
                "Slots": "[]",
                "Storage": 3035608,
                "StorageSlope": 0,
                "Runid": "0711f42e392386674313f264f371b1288d2f800f",
                "Connected": 1
            },
            {
                "Keys": 0,
                "Role": 0,
                "ShardId": "2",
                "ShardName": "crs-7ponppu3-001-01",
                "Slots": "[\"5461-10922\"]",
                "Storage": 3160280,
                "StorageSlope": 0.018086727708578,
                "Runid": "abf321a8ee9d4117f55b84ad9d70c3ef53f485af",
                "Connected": 1
            },
            {
                "Keys": 0,
                "Role": 1,
                "ShardId": "2",
                "ShardName": "crs-7ponppu3-001-02",
                "Slots": "[]",
                "Storage": 3036632,
                "StorageSlope": 0,
                "Runid": "9b8d9ec9ac452ab5a866cc8331a92c16e95e9dda",
                "Connected": 1
            },
            {
                "Keys": 0,
                "Role": 0,
                "ShardId": "3",
                "ShardName": "crs-7ponppu3-002-01",
                "Slots": "[\"10923-16383\"]",
                "Storage": 3055440,
                "StorageSlope": -0.015687562525272,
                "Runid": "3f299a51ad59fe7781e98b9ce6c807332931119b",
                "Connected": 1
            },
            {
                "Keys": 0,
                "Role": 1,
                "ShardId": "3",
                "ShardName": "crs-7ponppu3-002-02",
                "Slots": "[]",
                "Storage": 3035608,
                "StorageSlope": 0,
                "Runid": "0498c543d7a49d8f7fc27706edbaf5b38fcb31f6",
                "Connected": 1
            }
        ],
        "TotalCount": 6,
        "RequestId": "ca3000b6-bb8a-41fd-9074-11b5fda52d9f"
    }
}
```

