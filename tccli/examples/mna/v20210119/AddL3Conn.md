**Example 1: 示例1**



Input: 

```
tccli mna AddL3Conn --cli-unfold-argument  \
    --Cidr1 173.12.0.0/16 \
    --Cidr2 173.13.0.0/16 \
    --DeviceId1 abc \
    --DeviceId2 cde \
    --Description this is a test rule
```

Output: 
```
{
    "Response": {
        "L3ConnId": "abc",
        "RequestId": "abc"
    }
}
```

