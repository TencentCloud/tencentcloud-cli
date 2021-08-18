**Example 1: 查询存量服务测试**



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

