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
    "RequestId": "08238fd3-3691-4f8a-958d-241dd1d8c3a2",
    "Result": "lane-5yrdkb8v"
}
```

