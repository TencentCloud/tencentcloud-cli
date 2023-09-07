**Example 1: 修改边界防火墙开关(旁路、串行)**

修改边界防火墙开关(旁路、串行)

Input: 

```
tccli cfw ModifyEdgeIpSwitch --cli-unfold-argument  \
    --Enable 1 \
    --EdgeIpSwitchLst.0.PublicIp 1.1.1.1 \
    --EdgeIpSwitchLst.0.SubnetId subnet-11111111 \
    --EdgeIpSwitchLst.0.EndpointIp  \
    --EdgeIpSwitchLst.0.SwitchMode 0
```

Output: 
```
{
    "Response": {
        "RequestId": "11112222"
    }
}
```

