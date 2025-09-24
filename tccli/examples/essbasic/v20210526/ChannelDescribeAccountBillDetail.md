**Example 1: 查询该第三方平台子客账号绑定中、剩余可绑定账号等套餐使用情况**

查询平台子客账号绑定中、剩余可绑定账号等套餐使用情况

Input: 

```
tccli essbasic ChannelDescribeAccountBillDetail --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyOrganizationId org_dianziqian \
    --Agent.AppId yDCWpUUckpvv76rqUxjIE8qvXHjCqG4t
```

Output: 
```
{
    "Response": {
        "BoundAccountsNumber": 1,
        "InvalidAccountsNumber": 0,
        "RemainAvailableAccountsNumber": 9,
        "RequestId": "d8e66faf-6a5e-4592-9a8e-180b00577571",
        "TotalBuyAccountsNumber": 0,
        "TotalGiftAccountsNumber": 9
    }
}
```

