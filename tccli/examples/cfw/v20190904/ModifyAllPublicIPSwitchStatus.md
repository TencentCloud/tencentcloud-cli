**Example 1: 互联网边界防火墙一键开关**



Input: 

```
tccli cfw ModifyAllPublicIPSwitchStatus --cli-unfold-argument  \
    --Status 0 \
    --FireWallPublicIPs xx
```

Output: 
```
{
    "Response": {
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

