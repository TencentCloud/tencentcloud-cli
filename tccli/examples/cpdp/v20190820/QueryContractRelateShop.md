**Example 1: 查询合同可关联门店接口成功示例**

查询合同可关联门店接口成功

Input: 

```
tccli cpdp QueryContractRelateShop --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --ContractId C0001
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "ErrCode": "0",
        "ErrMessage": "操作成功",
        "Result": [
            {
                "IsChecked": "1",
                "ShopNo": "S0001",
                "ShopName": "南山店",
                "Province": "广东",
                "CityId": "440300",
                "Address": "大学城",
                "TerminalCount": "1",
                "ShopStatus": "1"
            }
        ]
    }
}
```

