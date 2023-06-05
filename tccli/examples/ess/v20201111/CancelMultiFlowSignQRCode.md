**Example 1: 取消一码多扫二维码**

取消一码多扫二维码

Input: 

```
tccli ess CancelMultiFlowSignQRCode --cli-unfold-argument  \
    --Operator.UserId test \
    --QrCodeId test
```

Output: 
```
{
    "Response": {
        "RequestId": "test"
    }
}
```

