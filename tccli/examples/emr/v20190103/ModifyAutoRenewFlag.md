**Example 1: 开启关闭自动续费接口**



Input: 

```
tccli emr ModifyAutoRenewFlag --cli-unfold-argument  \
    --InstanceId emr-xxxxx \
    --ResourceIds emr-vm-xxxx1 emr-vm-xxxx2 emr-vm-xxxx3 \
    --RenewFlag NOTIFY_AND_MANUAL_RENEW
```

Output: 
```
{
    "Response": {
        "RequestId": "4d701c1e-8507-47e1-8c69-a8f06a236f24"
    }
}
```

