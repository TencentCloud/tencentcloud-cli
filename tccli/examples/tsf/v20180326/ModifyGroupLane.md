**Example 1: 更新部署组泳道信息**



Input: 

```
tccli tsf ModifyGroupLane --cli-unfold-argument  \
    --GroupId group-2vzee8vp \
    --LaneList.0.GroupId group-2vzee8vp \
    --LaneList.0.LaneId lane-yxld94dy \
    --LaneList.0.Entrance True \
    --LaneList.1.GroupId group-2vzee8vp \
    --LaneList.1.LaneId lane-alb9gjxv \
    --LaneList.1.Entrance False
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "794f1bce-97a8-447b-9059-e179b550f13d"
    }
}
```

