**Example 1: 请求示例**

获取集群版实例分片信息

Input: 

```
tccli redis DescribeInstanceShards --cli-unfold-argument  \
    --InstanceId crs-7pon**** \
    --FilterSlave True
```

Output: 
```
{
    "Response": {
        "InstanceShards": [
            {
                "Connected": 1,
                "Keys": 274171,
                "Role": 0,
                "Runid": "edd1020ca1e3767c0d281d205964d168a2f5XXXX",
                "ShardId": "1",
                "ShardName": "crs-7pon****-001-02",
                "Slots": "[\"0-5460\"]",
                "Storage": 92353816,
                "StorageSlope": 0
            },
            {
                "Connected": 1,
                "Keys": 272958,
                "Role": 0,
                "Runid": "8f8b3760bfbea22e0fad8a0a9575d7716801XXXX",
                "ShardId": "3",
                "ShardName": "crs-XXXXXXXX-003-01",
                "Slots": "[\"10923-16383\"]",
                "Storage": 92096256,
                "StorageSlope": 0
            },
            {
                "Connected": 1,
                "Keys": 273074,
                "Role": 0,
                "Runid": "b6ed2e93ed754054f06220b995d42f4a07c2XXXX",
                "ShardId": "2",
                "ShardName": "crs-XXXXXXXX-002-01",
                "Slots": "[\"5461-10922\"]",
                "Storage": 92149456,
                "StorageSlope": 0
            }
        ],
        "RequestId": "9a57167a-f1a3-47ad-XXXX-b0ad835630a5",
        "TotalCount": 3
    }
}
```

