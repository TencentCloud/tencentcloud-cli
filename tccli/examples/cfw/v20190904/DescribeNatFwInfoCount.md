**Example 1: 获取当前用户接入nat防火墙的所有子网数及natfw实例个数**



Input: 

```
tccli cfw DescribeNatFwInfoCount --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "NatFwInsCount": 3,
        "SubnetCount": 3,
        "OpenSwitchCount": 3,
        "ReturnMsg": "success",
        "RequestId": "50e39f16-3b3a-4c66-b76e-1705449ba828"
    }
}
```

