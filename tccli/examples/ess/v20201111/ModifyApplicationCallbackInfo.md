**Example 1: 删除不存在的应用回调配置失败**

删除应用回调配置，对应的回调地址不存在，返回失败

Input: 

```
tccli ess ModifyApplicationCallbackInfo --cli-unfold-argument  \
    --Operator.UserId y******************g \
    --CallbackInfo.CallbackUrl https://yy.qq.com/ \
    --OperateType 2
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "当前配置不存在"
        },
        "RequestId": "s169*****2"
    }
}
```

**Example 2: 删除应用回调配置**

删除应用回调配置，成功只会返回RequestId

Input: 

```
tccli ess ModifyApplicationCallbackInfo --cli-unfold-argument  \
    --Operator.UserId y******************g \
    --CallbackInfo.CallbackUrl https://y.qq.com/ \
    --OperateType 2
```

Output: 
```
{
    "Response": {
        "RequestId": "s1*****9"
    }
}
```

**Example 3: 新增应用回调配置**

新增一条应用回调配置，成功只会返回RequestId

Input: 

```
tccli ess ModifyApplicationCallbackInfo --cli-unfold-argument  \
    --Operator.UserId y******************g \
    --CallbackInfo.CallbackUrl https://y.qq.com/ \
    --CallbackInfo.CallbackKey A******************B \
    --CallbackInfo.CallbackToken A********C \
    --OperateType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "s1*****9"
    }
}
```

