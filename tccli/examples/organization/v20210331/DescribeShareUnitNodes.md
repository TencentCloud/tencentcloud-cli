**Example 1: 获取共享单元部门列表**



Input: 

```
tccli organization DescribeShareUnitNodes --cli-unfold-argument  \
    --UnitId shareUnit-pj9**1f0du \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": "2026-02-02 21:21:52",
                "ShareNodeId": 10001
            }
        ],
        "Total": 1,
        "RequestId": "628aeb1f-7645-4c9f-9bcb-31484b89a8d4"
    }
}
```

