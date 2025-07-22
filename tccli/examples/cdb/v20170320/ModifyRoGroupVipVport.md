**Example 1: 修改Ro组的vip和vport**

修改Ro组的vip和vport

Input: 

```
tccli cdb ModifyRoGroupVipVport --cli-unfold-argument  \
    --UGroupId cdbrg-*** \
    --DstIp 1.2.3.4 \
    --DstPort 3307
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

