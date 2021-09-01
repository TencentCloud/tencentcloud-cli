**Example 1: 机器审核详情列表**



Input: 

```
tccli ims DescribeImsList --cli-unfold-argument  \
    --PageIndex 0 \
    --PageSize 0 \
    --Filters.0.Name "xx" \
    --Filters.0.Values "xx" "xx"
```

Output: 
```
{
    "Response": {
        "TotalCount": 312,
        "ImsDetailSet": {
            "UpdateUser": 0,
            "UpdateTime": "xx",
            "ModerationTime": 0,
            "ContentId": 0,
            "EvilType": 0,
            "Content": "xx",
            "DataSource": 0
        },
        "RequestId": "xx"
    }
}
```

