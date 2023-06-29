**Example 1: 获取告警策略列表**

获取告警策略列表

Input: 

```
tccli tcss DescribeWarningRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "WarningRules": [
            {
                "Type": "IMG_VIRUS",
                "Switch": "ON",
                "BeginTime": "10:00",
                "EndTime": "20:00",
                "ControlBits": "110"
            }
        ],
        "RequestId": "fee1bdb0-c13f-4c65-b567-8e270df211c1"
    }
}
```

