**Example 1: 修改防火墙开关**



Input: 

```
tccli cfw ModifyPublicIPSwitchStatus --cli-unfold-argument  \
    --FireWallPublicIP 1.2.3.4 \
    --Status 1
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

