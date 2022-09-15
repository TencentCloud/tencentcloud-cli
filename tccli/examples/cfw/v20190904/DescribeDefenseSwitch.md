**Example 1: 获取入侵防御按钮列表**



Input: 

```
tccli cfw DescribeDefenseSwitch --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "BasicRuleSwitch": 1,
        "BaselineAllSwitch": 1,
        "VirtualPatchSwitch": 1,
        "TiSwitch": 1,
        "HistoryOpen": 1
    }
}
```

