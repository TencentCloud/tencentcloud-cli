**Example 1: 本示例将实例计费模式切换为按小时后付费模式。**

本示例用于切换一个实例的计费模式。

Input: 

```
tccli cvm ModifyInstancesChargeType --cli-unfold-argument  \
    --InstanceChargeType POSTPAID_BY_HOUR \
    --InstanceIds ins-r8hr2upy
```

Output: 
```
{
    "Response": {
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```

**Example 2: 本示例将实例计费模式切换为预付费模式，且时长为1个月。**

本示例用于切换一个实例的计费模式。

Input: 

```
tccli cvm ModifyInstancesChargeType --cli-unfold-argument  \
    --InstanceChargeType PREPAID \
    --InstanceIds ins-r8hr2upy \
    --InstanceChargePrepaid.Period 1
```

Output: 
```
{
    "Response": {
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```

