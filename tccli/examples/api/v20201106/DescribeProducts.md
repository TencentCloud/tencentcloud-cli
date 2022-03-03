**Example 1: 查询产品信息**



Input: 

```
tccli api DescribeProducts --cli-unfold-argument  \
    --Limit 5 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 39,
        "Products": [
            {
                "Name": "cvm"
            },
            {
                "Name": "vpc"
            },
            {
                "Name": "faceid"
            },
            {
                "Name": "cp"
            },
            {
                "Name": "cls"
            }
        ],
        "RequestId": "bae5aa6f-f179-4fd6-95a1-e939c3c0b253"
    }
}
```

