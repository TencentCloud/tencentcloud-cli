**Example 1: 创建策略**

创建策略

Input: 

```
tccli organization CreatePolicy --cli-unfold-argument  \
    --Content {"version":"2.0","statement":[{"effect":"allow","action":"*","resource":"*"}]} \
    --Description FullAccessPolicy \
    --Name FullAccessPolicy \
    --Type SERVICE_CONTROL_POLICY
```

Output: 
```
{
    "Response": {
        "PolicyId": 100001,
        "RequestId": "fd498970-3ffb-440e-a3bf-f6faa43eeb08"
    }
}
```

