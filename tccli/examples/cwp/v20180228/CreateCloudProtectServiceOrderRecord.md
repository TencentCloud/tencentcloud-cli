**Example 1: 确认收货**

云护航服务使用完成后，确认收货，后续隐藏服务订单

Input: 

```
tccli cwp CreateCloudProtectServiceOrderRecord --cli-unfold-argument  \
    --ResourceIds cwpesc-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "6664048c-808a-1f57-2187-4553f4157426",
        "Success": [
            "cwpesc-xxxxxxxx"
        ]
    }
}
```

