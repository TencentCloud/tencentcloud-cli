**Example 1: Modifying the weight of the real server bound to a layer-4 listener**

This example shows you how to change the weight of the real server `ins-dm4xtz0i` (bound port: 334) bound to the listener `lbl-d1ubsydq` to 8.

Input: 

```
tccli clb ModifyTargetWeight --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0\
    --ListenerId lbl-d1ubsydq\
    --Targets.0.InstanceId ins-dm4xtz0i\
    --Targets.0.Port 334\
    --Weight 8
```

Output: 
```
{
    "Response": {
        "RequestId": "85c7b3e8-7fd8-4c62-8b3b-7ba52d7a1dca"
    }
}
```

