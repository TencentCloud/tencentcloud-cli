**Example 1: 重置实例机型**

当目前的机型配置不满足业务需求时，您可以重新调整其规格。

Input: 

```
tccli cvm ResetInstancesType --cli-unfold-argument  \
    --InstanceType S5.16XLARGE256 \
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

