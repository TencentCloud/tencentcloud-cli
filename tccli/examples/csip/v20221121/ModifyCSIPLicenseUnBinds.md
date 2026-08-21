**Example 1: 解绑主机授权**



Input: 

```
tccli csip ModifyCSIPLicenseUnBinds --cli-unfold-argument  \
    --InstanceIDs ins-78ip**** \
    --IsAll False
```

Output: 
```
{
    "Response": {
        "FailedList": [],
        "FailedNum": 0,
        "SuccessNum": 1,
        "Total": 1,
        "RequestId": "6d41bb64-0e86-4460-a952-0515b0162566"
    }
}
```

