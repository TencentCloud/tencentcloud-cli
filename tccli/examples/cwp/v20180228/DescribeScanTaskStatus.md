**Example 1: 示例**



Input: 

```
tccli cwp DescribeScanTaskStatus --cli-unfold-argument  \
    --ModuleType Malware
```

Output: 
```
{
    "Response": {
        "RequestId": "f1dd9f5e-4ac0-48a7-9410-c86d24656d9a",
        "State": {
            "Scanning": "扫描中",
            "Ok": "扫描成功",
            "Stop": "扫描中止",
            "Fail": "扫描失败"
        }
    }
}
```

