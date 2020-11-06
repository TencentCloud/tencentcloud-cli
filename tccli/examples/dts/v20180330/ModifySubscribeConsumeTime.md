**Example 1: Modifying the consumption starting time point of data subscription channel**

This example shows you how to reset the data starting point of a data subscription channel, so that the SDK can consume data starting at this time point.

Input: 

```
tccli dts ModifySubscribeConsumeTime --cli-unfold-argument  \
    --SubscribeId subs-ieuwi83j2e \
    --ConsumeStartTime '2019-10-26 00:00:00'
```

Output: 
```
{
    "Response": {
        "RequestId": "14a719b5-ffb34ab6-816c43c1-8c6a23eb"
    }
}
```

