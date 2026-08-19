**Example 1: 查询腾讯云指定CLB实例对应的七层转发规则列表**



Input: 

```
tccli csip DescribeClbListenerRules --cli-unfold-argument  \
    --AssetID lbl-m*km*k*0 \
    --MemberId mem-68b*08*a6*268000 \
    --Limit 1 \
    --Offset 0 \
    --Order UpdateTime \
    --By Desc
```

Output: 
```
{
    "Response": {
        "Rules": [],
        "TotalCount": 0,
        "RequestId": "9cbf28fa-7180-432f-98df-85891abb6db0"
    }
}
```

