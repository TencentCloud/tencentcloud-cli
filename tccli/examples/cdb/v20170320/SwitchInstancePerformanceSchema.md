**Example 1: 开启实例PFS功能**

成功开启实例PFS功能

Input: 

```
tccli cdb SwitchInstancePerformanceSchema --cli-unfold-argument  \
    --InstanceId cdb-1yrgrdmr \
    --Operation enable \
    --Instruments wait \
    --Consumers events_statements_history
```

Output: 
```
{
    "Response": {
        "JobId": "148123648",
        "RequestId": "610d5d6a-402b-457e-bab3-a7678ac94770"
    }
}
```

