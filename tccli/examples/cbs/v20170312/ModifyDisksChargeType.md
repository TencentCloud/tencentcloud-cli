**Example 1: 切换云硬盘的计费模式**

本示例用于切换一个云硬盘的计费模式（将按量计费模式转换为包年包月模式）。

Input: 

```
tccli cbs ModifyDisksChargeType --cli-unfold-argument  \
    --DiskIds disk-jwk0zvrg \
    --DiskChargePrepaid.Period 1
```

Output: 
```
{
    "Response": {
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```

