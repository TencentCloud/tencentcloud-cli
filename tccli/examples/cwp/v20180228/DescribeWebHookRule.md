**Example 1: 获取企微机器人规则详情**

获取企微机器人规则详情

Input: 

```
tccli cwp DescribeWebHookRule --cli-unfold-argument  \
    --Id 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "RuleId": 0,
            "RuleName": "test",
            "HookAddr": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=cbe03861-a8c6-48df-e34c-443c34be0db5",
            "RuleRemark": "",
            "RuleItems": [
                {
                    "Type": 11,
                    "ControlBit": "01111"
                }
            ],
            "HostLabels": [
                {
                    "Type": 4,
                    "Values": []
                }
            ],
            "HostIds": [
                "747c393e-f771-47ca-af1a-cc36b88f107a"
            ],
            "IsDisabled": 0
        },
        "RequestId": "747c393e-f771-47ca-af0a-cc36b88f107a"
    }
}
```

