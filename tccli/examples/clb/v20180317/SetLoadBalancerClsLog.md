**Example 1: Deleting a CLS topic**

This example shows you how to delete the CLS topic of a CLB instance.

Input: 

```
tccli clb SetLoadBalancerClsLog --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2r00\
    --LogSetId \
    --LogTopicId 
```

Output: 
```
{
    "Response": {
        "RequestId": "78a40898-8210-44c7-8bc6-f83e50878d12"
    }
}
```

**Example 2: Setting a CLS topic**

This example shows you how to add or modify the CLS topic of a CLB instance.

Input: 

```
tccli clb SetLoadBalancerClsLog --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2r00\
    --LogSetId xxxx-xx-xx-xx-xxxxxxxx\
    --LogTopicId xxxx-xx-xx-xx-yyyyyyyy
```

Output: 
```
{
    "Response": {
        "RequestId": "78a40898-8210-44c7-8bc6-f83e50878d12"
    }
}
```

