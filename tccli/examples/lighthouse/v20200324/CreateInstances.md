**Example 1: 通过API创建轻量应用服务器**

用户可以通过调用此接口，创建预付费的轻量应用服务器。

Input: 

```
tccli lighthouse CreateInstances --cli-unfold-argument  \
    --BundleId bundle_gen_03 \
    --BlueprintId lhbp-g0tn7djh \
    --InstanceChargePrepaid.Period 1 \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_MANUAL_RENEW
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "lhins-hx5wjw4g"
        ],
        "RequestId": "232b2817-ec08-43f3-8d78-41b1bfb6082c"
    }
}
```

