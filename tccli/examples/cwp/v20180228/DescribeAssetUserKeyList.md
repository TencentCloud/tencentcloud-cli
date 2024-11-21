**Example 1: 获取主机账号Key列表**



Input: 

```
tccli cwp DescribeAssetUserKeyList --cli-unfold-argument  \
    --Name name1 \
    --Offset 0 \
    --Limit 10 \
    --Uuid 6cf3c132-aaa-bbbb-b08d-98be9421372a \
    --Quuid 6cf3c132-aaa-bbbb-b08d-98be9421372a
```

Output: 
```
{
    "Response": {
        "Keys": [
            {
                "Value": "root",
                "Comment": "desc of value1",
                "EncryptType": "aes"
            }
        ],
        "Total": 1,
        "RequestId": "8564b09e-0e04-4516-bb59-db09742503c2"
    }
}
```

