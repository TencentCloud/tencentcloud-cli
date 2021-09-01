**Example 1: 续费CDH实例**



Input: 

```
tccli cvm RenewHosts --cli-unfold-argument  \
    --HostChargePrepaid.Period 1 \
    --HostChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW \
    --HostIds host-ey16rkyg
```

Output: 
```
{
    "Response": {}
}
```

