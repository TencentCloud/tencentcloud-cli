**Example 1: 创建网络设备型号**



Input: 

```
tccli chc CreateNetDeviceModel --cli-unfold-argument  \
    --ModelDetail.DevModel XXX-test \
    --ModelDetail.DevWidth 370－446 \
    --ModelDetail.DevDepth ≤1000 \
    --ModelDetail.DevWeight ≤50 \
    --ModelDetail.MountEar 否 \
    --ModelDetail.AccordCCC 是 \
    --ModelDetail.PassNetwork 是 \
    --ModelDetail.PowerportType C13 \
    --ModelDetail.PowerModule 交流 \
    --ModelDetail.PowermoduleNum 2 \
    --ModelDetail.PowermodulePosition 设备后端 \
    --ModelDetail.HighVoltageAdapt 否 \
    --ModelDetail.PowerEnergy 350 \
    --ModelDetail.InwindPosition 前 \
    --ModelDetail.OutwindPosition 后 \
    --ModelDetail.BusinessPortPosition 后 \
    --ModelDetail.LineManager 否 \
    --ModelDetail.DevHeight 2
```

Output: 
```
{
    "Response": {
        "DevModel": "XXX-test",
        "RequestId": "24943157-d39d-44b7-ad4f-c9498f6a3b23",
        "Version": "V1"
    }
}
```

