**Example 1: 创建临时设备退出工单**



Input: 

```
tccli chc CreateSpeciallyQuitWorkOrder --cli-unfold-argument  \
    --IdcId 159 \
    --DeviceType otherDevice \
    --HandoverMethod 2 \
    --CustomerReceipt.PickUpStuff 张三 \
    --CustomerReceipt.PickUpStuffContact 16611111111 \
    --CustomerReceipt.PickUpStuffIDCard 632525198112198139 \
    --CustomerReceipt.PickUpTime 2025-12-11 12:00:00 \
    --Remark 测试xzh111 \
    --OtherDeviceList.0.DeviceSn 20250403chc1222 \
    --OtherDeviceList.0.TypeName 移动硬盘 \
    --OtherDeviceList.0.Manufacturer 华为 \
    --OtherDeviceList.0.HardwareMemo xx设备第二个硬盘 \
    --OtherDeviceList.1.DeviceSn 20240101chc0008 \
    --OtherDeviceList.1.TypeName 其他 \
    --OtherDeviceList.1.HardwareMemo xxx设备第3个xx
```

Output: 
```
{
    "Response": {
        "RequestId": "f8fedcd3-198f-4ac5-be69-1b54ae62601d",
        "WorkOrderSet": [
            {
                "OrderType": "quit",
                "ServiceType": "quit",
                "WorkOrderId": "ord-25041015202483289"
            },
            {
                "OrderType": "personnelVisit",
                "ServiceType": "quit",
                "WorkOrderId": "ord-25041015202481186"
            }
        ]
    }
}
```

