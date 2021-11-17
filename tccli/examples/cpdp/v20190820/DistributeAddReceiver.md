**Example 1: 分账添加分账接收方接口成功示例**

分账添加分账接收方接口成功

Input: 

```
tccli cpdp DistributeAddReceiver --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --MerchantNo M0001 \
    --Remark 备注
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "ErrCode": "0",
        "ErrMessage": "操作成功",
        "Result": {
            "MerchantNo": "M0001"
        }
    }
}
```

