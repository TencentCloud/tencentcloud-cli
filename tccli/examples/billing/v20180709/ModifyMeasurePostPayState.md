**Example 1: 变更计量后付费按量计费策略**

无

Input: 

```
tccli billing ModifyMeasurePostPayState --cli-unfold-argument  \
    --ProductCode p_rav \
    --State 1 \
    --SubscriptionId rav-test111 \
    --Origin measure \
    --TriggerType 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "CurrentState": 1
        },
        "RequestId": "1f2800c4-a88c-4f32-b1fd-0a7368437610"
    }
}
```

