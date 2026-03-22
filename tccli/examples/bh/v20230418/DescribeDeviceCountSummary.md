**Example 1: 查询资产数统计数据**



Input: 

```
tccli bh DescribeDeviceCountSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DeviceCountSet": [
            {
                "Kind": 1,
                "Count": 10
            },
            {
                "Kind": 2,
                "Count": 20
            }
        ],
        "AppAssetCountSet": [
            {
                "Kind": 1,
                "Count": 1
            }
        ],
        "RequestId": "e4120a51-f130-4d11-a86c-fde256b347fb"
    }
}
```

