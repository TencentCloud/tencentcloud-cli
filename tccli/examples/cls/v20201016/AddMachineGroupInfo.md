**Example 1: 增量添加机器组ip或者label**



Input: 

```
tccli cls AddMachineGroupInfo --cli-unfold-argument  \
    --MachineGroupType.Values 10.0.60.184 \
    --MachineGroupType.Type ip \
    --GroupId 57f5808c-4a55-11eb-b378-0242ac130002
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

