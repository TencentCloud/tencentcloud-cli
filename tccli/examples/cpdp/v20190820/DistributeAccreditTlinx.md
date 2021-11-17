**Example 1: 分账授权申请接口成功示例**

分账授权申请接口成功

Input: 

```
tccli cpdp DistributeAccreditTlinx --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --AuthType 1 \
    --FullName 营业执照商户全称测试 \
    --Percent 200
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "ErrCode": "0",
        "ErrMessage": "操作成功",
        "Result": {
            "MerchantNo": "M0001",
            "ContractUrl": "https://www.tencent.com"
        }
    }
}
```

