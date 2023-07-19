**Example 1: 创建机器组**

创建机器组

Input: 

```
tccli cls CreateMachineGroup --cli-unfold-argument  \
    --GroupName testname \
    --MachineGroupType.Type ip \
    --MachineGroupType.Values 10.10.1.119
```

Output: 
```
{
    "Response": {
        "GroupId": "57f5808c-4a55-11eb-b378-0242ac130002",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

