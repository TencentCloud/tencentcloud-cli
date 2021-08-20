**Example 1: 查询用户信誉值**



Input: 

```
tccli pds DescribeNewUserAcquisition --cli-unfold-argument  \
    --ServiceParams.Openid xx \
    --ServiceParams.IP xx \
    --ServiceParams.PhoneNum xx
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

