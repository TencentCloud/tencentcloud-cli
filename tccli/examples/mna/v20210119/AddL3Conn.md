**Example 1: 示例1**



Input: 

```
tccli mna AddL3Conn --cli-unfold-argument  \
    --Cidr1 173.12.0.0/16 \
    --Cidr2 173.13.0.0/16 \
    --DeviceId1 mna-der44545r \
    --DeviceId2 cde \
    --Description this is a test rule
```

Output: 
```
{
    "Response": {
        "L3ConnId": "l3conn-h9boibynmp",
        "RequestId": "f0367096-b039-491c-b7eb-76669a2b22cf"
    }
}
```

