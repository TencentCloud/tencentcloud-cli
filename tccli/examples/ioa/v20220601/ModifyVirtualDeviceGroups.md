**Example 1: 将设备移动到普通的自定义分组**

将设备移动到普通的自定义分组

Input: 

```
tccli ioa ModifyVirtualDeviceGroups --cli-unfold-argument  \
    --DomainInstanceId 3 \
    --DeviceVirtualGroupId 10 \
    --DeviceList.0.DeviceMid C007D8BFA830C84A61965ABEC6FEDFD466A9E861 \
    --DeviceList.0.Operation 1 \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "17b01981-dff8-4267-b446-eefc4973acf4"
    }
}
```

