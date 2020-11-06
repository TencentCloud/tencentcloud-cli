**Example 1: 创建实例**



Input: 

```
tccli ecm RunInstances --cli-unfold-argument  \
    --ZoneInstanceCountISPSet.0.Zone ap-zhengzhou-1 \
    --ZoneInstanceCountISPSet.0.InstanceCount 2 \
    --ZoneInstanceCountISPSet.0.ISP CMCC \
    --ZoneInstanceCountISPSet.1.Zone ap-qingdao-1 \
    --ZoneInstanceCountISPSet.1.InstanceCount 1 \
    --ZoneInstanceCountISPSet.1.ISP CUCC \
    --InternetMaxBandwidthOut 50 \
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
        "InstanceIdSet": [
            "ein-197252sp",
            "ein-19725win",
            "ein-19623ash"
        ]
    }
}
```

