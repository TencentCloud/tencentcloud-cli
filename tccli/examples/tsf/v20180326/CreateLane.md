**Example 1: 创建泳道配置**



Input: 

```
tccli tsf CreateLane --cli-unfold-argument  \
    --LaneName app_lane \
    --Remark This is desc \
    --LaneGroupList.0.GroupId group-vwebgxzv \
    --LaneGroupList.0.Entrance True
```

Output: 
```
{
    "Response": {
        "RequestId": "681d3bab-f5fd-4a27-8b81-f65d6eda0238",
        "Result": "lane-vwdjqq29"
    }
}
```

