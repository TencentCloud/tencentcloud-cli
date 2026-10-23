**Example 1: 更新L3互通规则CIDR示例**



Input: 

```
tccli mna UpdateL3Cidr --cli-unfold-argument  \
    --L3ConnId l3conn-g4830c8tsh \
    --Cidr1 192.168.0.0/28 \
    --DeviceId1 mna-3jjzljbrsn \
    --DeviceId2 mna-05hq1wq4cf \
    --Cidr2 192.168.0.16/28
```

Output: 
```
{
    "Response": {
        "RequestId": "6585560f-568c-49f5-b789-04bd1eb1c5d6"
    }
}
```

