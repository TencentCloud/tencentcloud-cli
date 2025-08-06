**Example 1: 创建新服务器型号**



Input: 

```
tccli chc CreateServerModel --cli-unfold-argument  \
    --ModelDetail.DevModel XXX-TEST \
    --ModelDetail.DevNode 1 \
    --ModelDetail.DevHeight 9 \
    --ModelDetail.PowerEnergy 500 \
    --ModelDetail.PowerportType C14 \
    --ModelDetail.PowermoduleNum 2 \
    --ModelDetail.InwindPosition 前 \
    --ModelDetail.OutwindPosition 后 \
    --ModelDetail.NetportPosition 设备后端 \
    --ModelDetail.DevWidth <370 \
    --ModelDetail.DevDepth ≤780 \
    --ModelDetail.DevWeight ≤50 \
    --ModelDetail.PowerModule 兼容直流270DC和交流 \
    --ModelDetail.PowermodulePosition 设备后端 \
    --ModelDetail.NetportType 电口 \
    --ModelDetail.NetSpeed 千兆
```

Output: 
```
{
    "Response": {
        "DevModel": "XXX-TEST",
        "RequestId": "21f5aef1-4251-4f47-81de-aaf03c4cbfa5",
        "Version": "V1"
    }
}
```

