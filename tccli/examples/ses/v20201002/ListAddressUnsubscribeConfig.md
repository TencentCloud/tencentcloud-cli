**Example 1: 成功示例**



Input: 

```
tccli ses ListAddressUnsubscribeConfig --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "AddressUnsubscribeConfigList": [
            {
                "Address": "test@example.com",
                "Status": 1,
                "UnsubscribeConfig": "1"
            }
        ],
        "RequestId": "a4f27645-5c17-4f27-aa9f-746c2e2d821d",
        "Total": 1
    }
}
```

