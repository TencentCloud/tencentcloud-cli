**Example 1: ModifyTimerTask**



Input: 

```
tccli adp ModifyTimerTask --cli-unfold-argument  \
    --SpaceId default_space \
    --TimerId bbe5163d-7900-4230-941a-9b196a9bdfcc \
    --TimerTask.Profile.Prompt 2 \
    --UpdateMask.Paths profile.prompt
```

Output: 
```
{
    "Response": {
        "NextFireTime": "",
        "RequestId": "5475cddf-e2b5-4736-b8c3-bf4e2ae97356"
    }
}
```

