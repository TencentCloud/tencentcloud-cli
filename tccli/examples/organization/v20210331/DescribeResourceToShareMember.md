**Example 1: 获取与我共享的资源列表**



Input: 

```
tccli organization DescribeResourceToShareMember --cli-unfold-argument  \
    --Area guangzhou \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": "2021-03-06 17:11:30",
                "ResourceId": "shareResource-ew89er12d",
                "ProductResourceId": "vpc-ewd23dd",
                "Type": "vpc",
                "UnitId": "shareUnit-xhreofra2p",
                "UnitName": "test"
            }
        ],
        "RequestId": "34b1919e-ab09-4cc0-8f4b-b35f371c7c58",
        "Total": 1
    }
}
```

