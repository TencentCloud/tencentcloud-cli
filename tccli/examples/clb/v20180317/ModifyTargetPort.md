**Example 1: Modifying the port of a bound real server**

This example shows you how to change the port of the CVM instance `ins-dm4xtz0i` bound to the listener `lbl-d1ubsydq` from 233 to 334.

Input: 

```
tccli clb ModifyTargetPort --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0\
    --ListenerId lbl-d1ubsydq\
    --Targets.0.InstanceId ins-dm4xtz0i\
    --Targets.0.Port 233\
    --NewPort 334
```

Output: 
```
{
    "Response": {
        "RequestId": "a2764f3c-f173-421c-8e42-7b1e7a608ffd"
    }
}
```

