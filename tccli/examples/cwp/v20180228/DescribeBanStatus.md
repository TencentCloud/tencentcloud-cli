**Example 1: 获取阻断按钮状态**



Input: 

```
tccli cwp DescribeBanStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Status": 1,
        "ShowTips": false,
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

**Example 2: 新版BanStatus**

新版BanStatus

Input: 

```
tccli cwp DescribeBanStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "BanBlackIp": true,
        "BanByRule": false,
        "BanVulIp": true,
        "OpenSmartMode": true,
        "RequestId": "b76c888e-31cf-4dfe-b40a-0e3d30ee555e",
        "ShowTips": false,
        "Status": 2
    }
}
```

