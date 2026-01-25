**Example 1: 修改站点配置组的工作模式**

修改站点七层加速配置组、边缘函数配置组工作模式为版本管理。

Input: 

```
tccli teo ModifyZoneWorkMode --cli-unfold-argument  \
    --ZoneId zone-27********v1 \
    --WorkModeInfos.0.ConfigGroupType l7_acceleration \
    --WorkModeInfos.0.WorkMode version_control \
    --WorkModeInfos.1.ConfigGroupType edge_functions \
    --WorkModeInfos.1.WorkMode version_control
```

Output: 
```
{
    "Response": {
        "RequestId": "a06f52e7-2aab-4510-b2c2-1065bfb4414c"
    }
}
```

