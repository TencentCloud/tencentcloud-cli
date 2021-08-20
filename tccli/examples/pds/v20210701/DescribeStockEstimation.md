**Example 1: 查询用户信誉分**



Input: 

```
tccli pds DescribeStockEstimation --cli-unfold-argument  \
    --ServiceParams.Openid xx \
    --ServiceParams.PhoneNum xx \
    --ServiceParams.IP xx
```

Output: 
```
{
    "Response": {
        "ServiceRsp": {
            "Star": 0
        },
        "RequestId": "xx"
    }
}
```

