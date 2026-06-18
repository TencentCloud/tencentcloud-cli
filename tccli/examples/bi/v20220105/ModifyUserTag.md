**Example 1: 修改用户标签值**

修改用户标签值

Input: 

```
tccli bi ModifyUserTag --cli-unfold-argument  \
    --UserId abc \
    --TagList.0.Id 0 \
    --TagList.0.Name abc \
    --TagList.0.Value abc \
    --TagList.0.IsExternalManage True \
    --TagList.0.ManagePlatform abc \
    --TagList.0.ImportType abc
```

Output: 
```
{
    "Response": {
        "Msg": "abc",
        "Extra": "abc",
        "Data": "abc",
        "RequestId": "abc"
    }
}
```

