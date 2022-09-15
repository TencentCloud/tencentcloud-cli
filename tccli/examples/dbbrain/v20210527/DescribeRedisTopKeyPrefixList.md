**Example 1: 查询redis实例top key前缀列表**



Input: 

```
tccli dbbrain DescribeRedisTopKeyPrefixList --cli-unfold-argument  \
    --InstanceId cdb-test \
    --Date 2022-04-12 \
    --Product redis
```

Output: 
```
{
    "Response": {
        "RequestId": "8108c1c0-bbcc-11ec-adb9-eb9c1358e03a",
        "Items": [
            {
                "AveElementSize": 44,
                "Length": 864,
                "KeyPreIndex": "2028567046",
                "ItemCount": 5,
                "Count": 5,
                "MaxElementSize": 66
            }
        ],
        "Timestamp": 162072183
    }
}
```

