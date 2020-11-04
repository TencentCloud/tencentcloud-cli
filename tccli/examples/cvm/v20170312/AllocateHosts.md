**Example 1: 包年包月CDH实例购买**

购买付费模式为包年包月的CDH实例，指定位置在广州二区，购买一个月，到期自动续费，实例机型为HS1，购买一台

Input: 

```
tccli cvm AllocateHosts --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2\
    --HostChargeType PREPAID\
    --HostChargePrepaid.Period 1\
    --HostChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW\
    --HostType HS1\
    --HostCount 1
```

Output: 
```
{
    "Response": {
        "HostIdSet": [
            "host-lan4lb2k"
        ],
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

