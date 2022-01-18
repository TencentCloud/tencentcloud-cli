**Example 1: 在线烧录FPGA镜像**

本示例将由客户提供的FPGA镜像文件烧录到实例上的两块FPGA卡

Input: 

```
tccli cvm ProgramFpgaImage --cli-unfold-argument  \
    --InstanceId ins-r8hr2upy \
    --FPGAUrl fpga-test-123456.cos.ap-guangzhou.myqcloud.com/test.xclbin \
    --DBDFs 0000:00:08.0 0000:00:09.0
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270dfafb54a7"
    }
}
```

