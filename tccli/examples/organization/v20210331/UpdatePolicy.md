**Example 1: 编辑策略**

编辑策略

Input: 

```
tccli organization UpdatePolicy --cli-unfold-argument  \
    --Content {"version":"2.0","statement":[{"effect":"allow","action":"*","resource":"*"}]} \
    --Description FullAccessPolicy \
    --Name FullAccessPolicy \
    --PolicyId 100001
```

Output: 
```
{
    "Response": {
        "RequestId": "fd498970-3ffb-440e-a3bf-f6faa43eeb08"
    }
}
```

