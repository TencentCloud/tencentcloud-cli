**Example 1: 入侵防御开关相关**

接口返回常见入侵防御开关接口

Input: 

```
tccli cfw DescribeDefenseSwitch --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "BasicRuleSwitch": 0,
        "BaselineAllSwitch": 0,
        "TiSwitch": 0,
        "VirtualPatchSwitch": 0,
        "HistoryOpen": 0,
        "ReturnCode": 0,
        "ReturnMsg": "abc",
        "RequestId": "abc"
    }
}
```

