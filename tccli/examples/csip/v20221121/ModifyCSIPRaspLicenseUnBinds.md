**Example 1: 解绑RASP授权**



Input: 

```
tccli csip ModifyCSIPRaspLicenseUnBinds --cli-unfold-argument  \
    --InstanceIDs ins-78ip**** \
    --IsAll False
```

Output: 
```
{
    "Response": {
        "FailedList": [],
        "FailedNum": 0,
        "SuccessNum": 0,
        "Total": 0,
        "RequestId": "5d1c5e68-75a3-4b0d-bb23-9c65debf8b2e"
    }
}
```

