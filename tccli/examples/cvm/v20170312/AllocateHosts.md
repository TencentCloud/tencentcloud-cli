**Example 1: Purchasing a monthly subscription CDH instance**

This example shows you how to purchase 1 CDH instance with the following configuration. Billing method: monthly subscription; availability zone: Guangzhou Zone 2; subscription period: 1 month; renewal flag: auto-renewal upon expiration; instance model: HS1.

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

