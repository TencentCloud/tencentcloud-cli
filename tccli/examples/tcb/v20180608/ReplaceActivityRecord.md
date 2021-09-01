**Example 1: 更新活动详情**

更新活动详情

Input: 

```
tccli tcb ReplaceActivityRecord --cli-unfold-argument  \
    --ActivityId 1 \
    --Status 2 \
    --SubStatus 4323 \
    --ChannelToken 321 \
    --Channel qc_console
```

Output: 
```
{
    "Response": {
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351"
    }
}
```

