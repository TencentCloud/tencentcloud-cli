**Example 1: CreateCustomHeader**



Input: 

```
tccli gaap CreateCustomHeader --cli-unfold-argument  \
    --RuleId rule-18vhg67 \
    --Headers.0.HeaderName X-REAL_IP \
    --Headers.0.HeaderValue $remote_addr \
    --Headers.1.HeaderName X-FORWORD-IP \
    --Headers.1.HeaderValue 192.168.2.101
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

