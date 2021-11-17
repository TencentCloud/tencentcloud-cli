**Example 1: 分账结果查询接口成功示例**

分账结果查询接口成功

Input: 

```
tccli cpdp DistributeQuery --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --OrderNo sz2021101244 \
    --Type 1
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "ErrCode": "0",
        "ErrMessage": "提交成功",
        "Result": {
            "Orders": [
                {
                    "OutDistributeNo": "123",
                    "DistributeNo": "456",
                    "OrderNo": "789",
                    "Status": "1",
                    "InDate": "2021-10-01",
                    "Remark": "备注",
                    "Details": [
                        {
                            "MerchantNo": "M0001",
                            "Amount": "100",
                            "Remark": "备注"
                        }
                    ]
                }
            ]
        }
    }
}
```

