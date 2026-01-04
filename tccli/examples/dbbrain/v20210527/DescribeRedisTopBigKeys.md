**Example 1: 查询redis实例大key列表**



Input: 

```
tccli dbbrain DescribeRedisTopBigKeys --cli-unfold-argument  \
    --InstanceId crs-occia4d6 \
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
                "ShardId": "1",
                "Type": "set",
                "AveElementSize": 15894,
                "Length": 93542932,
                "ItemCount": 4999,
                "Encoding": "skiplist",
                "ExpireTime": 0,
                "MaxElementSize": 34431,
                "Key": "test-key",
                "Db": 0
            }
        ],
        "Timestamp": 162072183
    }
}
```

