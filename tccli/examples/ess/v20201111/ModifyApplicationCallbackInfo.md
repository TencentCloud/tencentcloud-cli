**Example 1: 修改应用callbackinfo**

修改应用callbackinfo

Input: 

```
tccli ess ModifyApplicationCallbackInfo --cli-unfold-argument  \
    --Operator.UserId xxx \
    --CallbackInfo.CallbackUrl https://y.qq.com/ \
    --CallbackInfo.Token xxx222xxx \
    --OperateType 2
```

Output: 
```
{
    "Response": {
        "RequestId": "s1675154686215203499"
    }
}
```

