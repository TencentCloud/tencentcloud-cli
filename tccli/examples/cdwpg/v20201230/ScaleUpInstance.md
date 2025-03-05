**Example 1: 1**



Input: 

```
tccli cdwpg ScaleUpInstance --cli-unfold-argument  \
    --InstanceId cdwpg-xxxxx \
    --InstanceName test1 \
    --Case vm \
    --ModifySpec.Type cn \
    --ModifySpec.SpecName S_8_32_S \
    --ModifySpec.Count 4 \
    --ModifySpec.DiskSpec.DiskType CLOUD_SSD \
    --ModifySpec.DiskSpec.DiskSize 200 \
    --ModifySpec.DiskSpec.DiskCount 1
```

Output: 
```
{
    "Response": {
        "FlowId": 43,
        "RequestId": "errorstest",
        "ErrorMsg": "errorstest"
    }
}
```

