**Example 1: 分账请求接口成功示例**

分账请求接口成功

Input: 

```
tccli cpdp DistributeApply --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --OutDistributeNo D20211001001 \
    --DeveloperNo T20211001232100 \
    --Details.0.MerchantNo M0001 \
    --Details.0.Amount 100 \
    --Details.0.Remark 备注 \
    --Remark 说明
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "ErrCode": "0",
        "ErrMessage": "提交成功",
        "Result": {
            "OutDistributeNo": "D20211001001",
            "DistributeNo": "sz202110909",
            "OrderNo": "sz2021101244",
            "Status": "1",
            "Amount": "100",
            "InDate": "2021-10-08"
        }
    }
}
```

