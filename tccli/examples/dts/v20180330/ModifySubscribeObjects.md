**Example 1: Modifying the subscription rule of data subscription channel**

This example shows you how to modify the subscription rule of a data subscription, such as adding or removing certain tables.

Input: 

```
tccli dts ModifySubscribeObjects --cli-unfold-argument  \
    --SubscribeId subs-ieuwi83j2e \
    --SubscribeObjectType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "14a719b5-ffb34ab6-816c43c1-8c6a23eb",
        "AsyncRequestId": "19b514a7-816c43c1-ffb34ab6-8c6a23eb"
    }
}
```

