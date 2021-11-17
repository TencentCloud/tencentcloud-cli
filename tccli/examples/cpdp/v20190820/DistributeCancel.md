**Example 1: 分账撤销接口成功示例**

分账撤销接口成功

Input: 

```
tccli cpdp DistributeCancel --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --OutDistributeNo 123 \
    --OrderNo sz2021101244
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "ErrCode": "0",
        "ErrMessage": "提交成功",
        "Result": {}
    }
}
```

