**Example 1: 分账授权申请查询接口成功示例**

分账授权申请查询接口成功

Input: 

```
tccli cpdp DistributeAccreditQuery --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "ErrCode": "0",
        "ErrMessage": "操作成功",
        "Result": {
            "Status": "1",
            "Remark": "已开通",
            "ContractUrl": "https://www.tencent.com"
        }
    }
}
```

