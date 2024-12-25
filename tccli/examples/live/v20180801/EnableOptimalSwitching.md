**Example 1: 请求示例**

对该主备流启用择优调度。

Input: 

```
tccli live EnableOptimalSwitching --cli-unfold-argument  \
    --StreamName stream1 \
    --EnableSwitch 1
```

Output: 
```
{
    "Response": {
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

