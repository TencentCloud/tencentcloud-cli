**Example 1: 查询GPU可售规格及额度**

查询当前地域可售 GPU 规格与当前租户可购买额度。GPUType、CPU、Memory、GPUNum 必须同时提供或同时省略；精确过滤时按四项匹配。不返回底层机型、资源池或计费标签。总显存为单台全部 GPU 的显存之和。

Input: 

```
tccli ags DescribeGPUResourceSpecs --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "GPUResourceSpecSet": [
            {
                "GPUType": "5090d",
                "GPUTypeAlias": "NVIDIA RTX 5090 D",
                "GPUMemoryGiB": 64,
                "CPU": 64,
                "Memory": 192,
                "GPUNum": 2,
                "AvailableCount": 2
            }
        ],
        "TotalCount": 1,
        "RequestId": "request-example"
    }
}
```

**Example 2: 精确查询一个规格**

0 表示确认无可购买额度，AvailableCount 的单位是台。

Input: 

```
tccli ags DescribeGPUResourceSpecs --cli-unfold-argument  \
    --GPUType 5090d \
    --CPU 64 \
    --Memory 192 \
    --GPUNum 2 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "GPUResourceSpecSet": [
            {
                "GPUType": "5090d",
                "GPUTypeAlias": "NVIDIA RTX 5090 D",
                "GPUMemoryGiB": 64,
                "CPU": 64,
                "Memory": 192,
                "GPUNum": 2,
                "AvailableCount": 0
            }
        ],
        "TotalCount": 1,
        "RequestId": "request-example"
    }
}
```

**Example 3: 额度暂不可确认**

null 表示额度未知，不能转换成 0 或无限额度。

Input: 

```
tccli ags DescribeGPUResourceSpecs --cli-unfold-argument  \
    --GPUType 5090d \
    --CPU 64 \
    --Memory 192 \
    --GPUNum 2
```

Output: 
```
{
    "Response": {
        "GPUResourceSpecSet": [
            {
                "GPUType": "5090d",
                "GPUTypeAlias": "NVIDIA RTX 5090 D",
                "GPUMemoryGiB": 64,
                "CPU": 64,
                "Memory": 192,
                "GPUNum": 2,
                "AvailableCount": null
            }
        ],
        "TotalCount": 1,
        "RequestId": "request-example"
    }
}
```

