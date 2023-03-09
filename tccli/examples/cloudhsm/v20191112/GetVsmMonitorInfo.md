**Example 1: 获取VSM监控信息**

获取VSM监控信息

Input: 

```
tccli cloudhsm GetVsmMonitorInfo --cli-unfold-argument  \
    --ResourceId hsm-1234abcd \
    --ResourceName default-hsmName
```

Output: 
```
{
    "Response": {
        "MonitorInfo": [
            "xx"
        ],
        "RequestId": "xx"
    }
}
```

