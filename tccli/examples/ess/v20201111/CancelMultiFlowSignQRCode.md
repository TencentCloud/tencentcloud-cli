**Example 1: 取消一码多签签署码**

取消一码多签签署码

Input: 

```
tccli ess CancelMultiFlowSignQRCode --cli-unfold-argument  \
    --Operator.UserId yDxxxxxxx \
    --QrCodeId yDRvQxxxxxKC
```

Output: 
```
{
    "Response": {
        "RequestId": "1c75e86d-xxxxxxxxxx6f330a05e"
    }
}
```

**Example 2: 取消一码多签签署码-已失效**

废除取消一码多签签署码，若签署码已经失效，则返回操作失败。

Input: 

```
tccli ess CancelMultiFlowSignQRCode --cli-unfold-argument  \
    --Operator.UserId yDxxxxxxx \
    --QrCodeId yDRvQxxxxxKC
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied.QrInvalid",
            "Message": "签署二维码不可用，请检查后重试。"
        },
        "RequestId": "s169*****0872"
    }
}
```

