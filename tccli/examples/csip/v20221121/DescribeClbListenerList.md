**Example 1: 查询腾讯云指定CLB实例对应的监听器列表**



Input: 

```
tccli csip DescribeClbListenerList --cli-unfold-argument  \
    --AssetID lbl-**k*rkz0 \
    --MemberId mem-68b*08*a*5**8**0 \
    --Limit 1 \
    --Offset 0 \
    --Order UpdateTime \
    --By DESC
```

Output: 
```
{
    "Response": {
        "Listeners": [],
        "TotalCount": 0,
        "RequestId": "162b8b56-d63a-4371-869d-ff6992636efc"
    }
}
```

