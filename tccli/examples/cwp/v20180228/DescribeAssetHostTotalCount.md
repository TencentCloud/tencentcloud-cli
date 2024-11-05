**Example 1: 获取主机所有资源数量**



Input: 

```
tccli cwp DescribeAssetHostTotalCount --cli-unfold-argument  \
    --Uuid 6cf3c132-aaaa-bbbb-b08d-98be9421372a \
    --Quuid 6cf3c132-aaaa-bbbb-b08d-98be9421372a
```

Output: 
```
{
    "Response": {
        "Types": [
            {
                "Key": "key1",
                "Value": 10,
                "Desc": "desc of key1",
                "NewCount": 0
            }
        ],
        "RequestId": "8564b09e-0e04-4516-bb59-db09742503c2"
    }
}
```

