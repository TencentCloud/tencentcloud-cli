**Example 1: 获取联系人信息**



Input: 

```
tccli chc DescribeWorkOrderContactCollectList --cli-unfold-argument  \
    --Offset 3 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "ContactSet": [
            {
                "ContactName": "****",
                "ContactPhone": "*****"
            }
        ],
        "TotalCount": 21,
        "RequestId": "37f95f74-d476-43ab-af2d-bb9c32b5ee54"
    }
}
```

