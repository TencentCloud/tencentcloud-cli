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
        "NewsList": [
            {}
        ],
        "Count": 1,
        "RequestId": "1111111-2222-3333"
    }
}
```

