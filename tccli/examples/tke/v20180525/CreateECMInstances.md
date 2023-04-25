**Example 1: 创建边缘计算ECM机器**

创建边缘计算ECM机器

Input: 

```
tccli tke CreateECMInstances --cli-unfold-argument  \
    --ClusterID cls-xxxxx \
    --ZoneInstanceCountISPSet.0.Zone ap-zhengzhou-1 \
    --ZoneInstanceCountISPSet.0.InstanceCount 2 \
    --ZoneInstanceCountISPSet.0.ISP CMCC \
    --ImageId img-q9fy0if9 \
    --HostName oldhen_4986 \
    --ModuleId em-0vag13d1 \
    --InstanceName 直播弹幕 \
    --EnhancedService.SecurityService.Enabled false \
    --EnhancedService.MonitorService.Enabled false
```

Output: 
```
{
    "Response": {
        "RequestId": "d40cdb72-7bc0-4b48-b3aa-25e8401f6999",
        "EcmIdSet": [
            "ecm-197252sp",
            "ecm-19725win",
            "ecm-19623ash"
        ]
    }
}
```

