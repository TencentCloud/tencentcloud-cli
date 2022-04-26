**Example 1: 查询redis实例大key列表**



Input: 

```
tccli dbbrain DescribeRedisTopBigKeys --cli-unfold-argument  \
    --InstanceId cdb-test \
    --Date 2022-04-12 \
    --Product redis
```

Output: 
```
{
    "Response": {
        "RequestId": "8108c1c0-bbcc-11ec-adb9-eb9c1358e03a",
        "TopKeys": [
            {
                "Key": "test",
                "Type": "string",
                "Encoding": "string",
                "ExpireTime": 0,
                "Length": 72,
                "ItemCount": 1,
                "MaxElementSize": 10
            }
        ],
        "Timestamp": 162072183
    }
}
```

