**Example 1: 示例1**

查询激活码统计信息

Input: 

```
tccli iotexplorer DescribeVideoLicense --cli-unfold-argument  \
    --InstanceId aa
```

Output: 
```
{
    "Response": {
        "License": [
            {
                "ExpiresSoonCount": 0,
                "TotalCount": 0,
                "Type": "0_5_mbps",
                "UsedCount": 0
            },
            {
                "ExpiresSoonCount": 0,
                "TotalCount": 0,
                "Type": "1_mbps",
                "UsedCount": 0
            },
            {
                "ExpiresSoonCount": 0,
                "TotalCount": 0,
                "Type": "1_5_mbps",
                "UsedCount": 0
            },
            {
                "ExpiresSoonCount": 0,
                "TotalCount": 0,
                "Type": "2_mbps",
                "UsedCount": 0
            }
        ],
        "RequestId": "65ca8e0a-422a-4a7a-94bc-041ecd7abaf0"
    }
}
```

