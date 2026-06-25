**Example 1: 关闭NAT CCN集群模式防火墙开关**

关闭NAT CCN集群模式防火墙开关

Input: 

```
tccli cfw CloseClusterNatFwSwitch --cli-unfold-argument  \
    --NatInsId cfwnat-xxxxxxxx \
    --CcnId ccn-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "3b3a2e60-1b2c-4d3e-a4f5-6789abcdef01"
    }
}
```

