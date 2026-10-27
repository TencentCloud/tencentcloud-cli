**Example 1: 实例续费**



Input: 

```
tccli cvd RenewInstances --cli-unfold-argument  \
    --InstanceIds cvd-l0c69nmim85j8t1 \
    --ChargePrepaid.RenewFlag NOTIFY_AND_MANUAL_RENEW \
    --ChargePrepaid.Period 1
```

Output: 
```
{
    "Response": {
        "RequestId": "bc93710c-a2f9-4ebb-a62e-99eb38f57198"
    }
}
```

