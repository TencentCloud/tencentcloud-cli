**Example 1: 成功**

 

Input: 

```
tccli iss BatchOperateDevice --cli-unfold-argument  \
    --DeviceIds 2fa25418-****-4dde-****-5c2d****6d58 552fbaba-****-4a79-****-8504f****a53 6e448c42-****-4e2e-****-cc4a****15b9 e9b0b611-****-42a2-****-b30****b1c25 \
    --Cmd enable
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "28bdf2f7-****-4507-****-35f0****7ecf5"
        },
        "RequestId": "e7d070d7-8d22-4bfe-9873-6ff0ea331310"
    }
}
```

