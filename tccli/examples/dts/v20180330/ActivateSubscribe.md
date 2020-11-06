**Example 1: Configuring data subscription**

This example shows you how to configure a data subscription.

Input: 

```
tccli dts ActivateSubscribe --cli-unfold-argument  \
    --SubscribeId subs-ieuwi83j2e \
    --InstanceId cdb-9dijwkkw2 \
    --SubscribeObjectType 0
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "cafebabe-254f-11ea-8995-e92c139e6978"
    }
}
```

