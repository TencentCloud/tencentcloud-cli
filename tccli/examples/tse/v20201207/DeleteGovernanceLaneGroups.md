**Example 1: 删除泳道组**



Input: 

```
tccli tse DeleteGovernanceLaneGroups --cli-unfold-argument  \
    --InstanceId abc \
    --LaneGroups.0.Name abc \
    --LaneGroups.0.ID abc
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc"
    }
}
```

