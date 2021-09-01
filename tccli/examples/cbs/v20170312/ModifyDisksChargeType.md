**Example 1: 切换云盘的计费模式**

本示例用于切换一个云盘的计费模式（将按量计费云盘转换为包年包月云盘，并购买一个月时长）。

Input: 

```
tccli cbs ModifyDisksChargeType --cli-unfold-argument  \
    --DiskIds disk-jwk0zvrg \
    --DiskChargePostpaid True
```

Output: 
```
{
    "Response": {
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```

