**Example 1: 将云服务器实例从指定的置放群组中批量移除**

将云服务器实例 ins-23sh03x7 从置放群组 ps-c119a27y 中移除

Input: 

```
tccli cvm DeleteInstancesDisasterRecoverGroups --cli-unfold-argument  \
    --InstanceIds ins-23sh03x7 \
    --DisasterRecoverGroupIds ps-c119a27y
```

Output: 
```
{
    "Response": {
        "RequestId": "7c43bdac-5c17-4c35-8bb7-7d5aff400472"
    }
}
```

