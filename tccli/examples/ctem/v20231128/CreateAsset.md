**Example 1: 添加主机资产**



Input: 

```
tccli ctem CreateAsset --cli-unfold-argument  \
    --Os linux \
    --EnterpriseUid c546b0b87faf2f5ee93a9d0a069f5ed3 \
    --Ip 1.1.1.1 \
    --Country 中国 \
    --Province 广东省 \
    --City 深圳市 \
    --Isp 电信 \
    --CustomerId 100068
```

Output: 
```
{
    "Response": {
        "Id": 6870,
        "RequestId": "1113211e-02ab-bee7-b6d0-1903c307aa5c"
    }
}
```

