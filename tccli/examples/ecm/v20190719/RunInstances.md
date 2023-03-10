**Example 1: 创建实例**

使用模板创建实例

Input: 

```
tccli ecm RunInstances --cli-unfold-argument  \
    --ZoneInstanceCountISPSet.0.ISP CUCC \
    --ZoneInstanceCountISPSet.0.InstanceCount 1 \
    --ZoneInstanceCountISPSet.0.Zone ap-qingdao-1 \
    --ZoneInstanceCountISPSet.1.ISP CMCC \
    --ZoneInstanceCountISPSet.1.InstanceCount 2 \
    --ZoneInstanceCountISPSet.1.Zone ap-zhengzhou-1 \
    --HostName oldhen_4986 \
    --ImageId img-q9fy0if9 \
    --InternetMaxBandwidthOut 50 \
    --InstanceChargeType 0 \
    --EnhancedService.SecurityService.Enabled false \
    --EnhancedService.MonitorService.Enabled false \
    --InstanceName 直播弹幕 \
    --ModuleId em-0vag13d1
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

