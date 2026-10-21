**Example 1: 将成员设置为使用者**



Input: 

```
tccli fwm ModifyCfwShareRole --cli-unfold-argument  \
    --CfwShareRole user \
    --UserMemberId mem-1300846651-100037509558 \
    --SharerMemberId mem-1300846651-100011616646
```

Output: 
```
{
    "Response": {
        "RequestId": "818d5e2f-35ac-49a0-ba8c-3cdc4247e0eb"
    }
}
```

**Example 2: 将成员设置为共享者**



Input: 

```
tccli fwm ModifyCfwShareRole --cli-unfold-argument  \
    --CfwShareRole sharer \
    --UserMemberId mem-1300846651-100011616646
```

Output: 
```
{
    "Response": {
        "RequestId": "b2a220ad-d9f6-4bec-b4ee-da7d1dba98e6"
    }
}
```

