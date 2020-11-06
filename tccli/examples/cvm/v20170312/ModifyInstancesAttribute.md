**Example 1: 修改实例名称**

本示例用于修改两个实例的名称。

Input: 

```
tccli cvm ModifyInstancesAttribute --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy ins-5d8a23rs \
    --InstanceName Mysql_Server
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

