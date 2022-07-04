**Example 1: 修改CHC物理服务器的属性**

修改CHC物理服务器的属性

Input: 

```
tccli cvm ModifyChcAttribute --cli-unfold-argument  \
    --ChcIds chc-r8hr2upy chc-5d8a23rs \
    --InstanceName server1 \
    --DeviceType CHC_HS1
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

