**Example 1: 查询视立方产品动态**

概览页展示视立方产品动态

Input: 

```
tccli vcube DescribeNews --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Count": 4,
        "NewsList": [
            {
                "Id": 11
            },
            {
                "Id": 10
            }
        ],
        "RequestId": "02b4f484-89b7-44fd-9416-3d5bfd18ffab"
    }
}
```

