**Example 1: 创建泳道**



Input: 

```
tccli tsf CreateLane --cli-unfold-argument  \
    --LaneName test \
    --Remark test \
    --LaneGroupList.0.GroupId group-9yn758ad \
    --LaneGroupList.0.Entrance true
```

Output: 
```
{
    "Response": {
        "Result": "xx",
        "RequestId": "xx"
    }
}
```

