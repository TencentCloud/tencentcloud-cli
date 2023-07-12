**Example 1: 修改源站组信息**



Input: 

```
tccli teo ModifyOriginGroup --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali16 \
    --OriginGroupId origin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a \
    --OriginGroupName renameorigingroup \
    --ConfigurationType weight \
    --OriginType self \
    --OriginRecords.0.Record 1.2.3.4 \
    --OriginRecords.0.Weight 50 \
    --OriginRecords.0.Port 80 \
    --OriginRecords.1.Record 1.2.3.5 \
    --OriginRecords.1.Weight 50 \
    --OriginRecords.1.Port 80
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

