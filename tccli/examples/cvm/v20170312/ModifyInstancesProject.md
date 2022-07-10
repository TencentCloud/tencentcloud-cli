**Example 1: 修改两个实例所属的项目**

本示例用于修改两个实例所属的项目为指定的项目。

Input: 

```
tccli cvm ModifyInstancesProject --cli-unfold-argument  \
    --ProjectId 1045 \
    --InstanceIds ins-5d8a23rs ins-r8hr2upy
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

