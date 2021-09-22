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
        "RequestId": "xx",
        "State": {
            "Scanning": "",
            "Ok": "",
            "Stop": "",
            "Fail": ""
        }
    }
}
```

