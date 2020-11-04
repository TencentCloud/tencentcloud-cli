**Example 1: 修改两个实例所属的项目**

本示例用于修改两个实例所属的项目为指定的项目。

Input: 

```
tccli cvm ModifyInstancesProject --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy ins-5d8a23rs\
    --ProjectId 1045
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

