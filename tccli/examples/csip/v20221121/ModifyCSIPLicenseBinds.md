**Example 1: 绑定主机授权**



Input: 

```
tccli csip ModifyCSIPLicenseBinds --cli-unfold-argument  \
    --ResourceId csip-****-res-*** \
    --IsAll True \
    --LicenseType ENTERPRISE_HP \
    --InstanceIDs ins-78ip****
```

Output: 
```
{
    "Response": {
        "TaskId": 7525,
        "RequestId": "3288449b-a5a0-4ad4-8a74-8482ceb5e1e4"
    }
}
```

