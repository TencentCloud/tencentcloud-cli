**Example 1: 通知资源用尽**

通知资源用尽

Input: 

```
tccli tcb NotifyPackageOverrun --cli-unfold-argument  \
    --ResourceType abc \
    --ResourceName abc \
    --ResourceIndex abc \
    --UserUin abc \
    --UserAppId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

