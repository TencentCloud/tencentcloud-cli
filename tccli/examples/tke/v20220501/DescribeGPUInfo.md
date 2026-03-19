**Example 1: DescribeGPUInfo**

用于获取对应机型支持的GPU驱动，CUDA，CUDNN等版本信息

Input: 

```
tccli tke DescribeGPUInfo --cli-unfold-argument  \
    --InstanceType GN7.2XLARGE40 \
    --OsName tlinux3.1x86_64
```

Output: 
```
{
    "Response": {
        "GPUParams": [
            {
                "Driver": "470",
                "CUDA": "",
                "CUDNN": "",
                "MIGEnable": false,
                "Fabric": false
            }
        ],
        "RequestId": "ff772139-9790-4dbf-b4df-fb09339bb35b"
    }
}
```

