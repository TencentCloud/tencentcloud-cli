**Example 1: 示例1**



Input: 

```
tccli mna UpdateL3Cidr --cli-unfold-argument  \
    --L3ConnId l3conn-c0rkbqhig \
    --DeviceId1 mna-f8v7e6o432 \
    --Cidr1 192.168.0.16/28 \
    --DeviceId2 mna-f8v7e6o43g \
    --Cidr2 192.168.0.16/28
```

Output: 
```
{
    "Response": {
        "RequestId": "7ab57398-d79f-4195-b0d4-3aef1e43b9c7"
    }
}
```

