**Example 1: 测试**

测试

Input: 

```
tccli ioa DescribeDownloadHardwareChangeInfos --cli-unfold-argument  \
    --GroupId 92
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadURL": "https://ioa-download-1.test.com"
        },
        "RequestId": "21788424-8f47-48c4-a82a-ee7a22204a95"
    }
}
```

**Example 2: 示例1**



Input: 

```
tccli ioa DescribeDownloadHardwareChangeInfos --cli-unfold-argument  \
    --EndTime 2022-12-30 \
    --GroupId 392 \
    --BeginTime 2022-10-30
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadURL": "https://ioa-download-1.test.com"
        },
        "RequestId": "1c040b34-2514-4211-85a2-7d1f311ee798"
    }
}
```

