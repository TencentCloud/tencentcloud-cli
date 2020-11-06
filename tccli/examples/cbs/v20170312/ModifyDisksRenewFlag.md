**Example 1: 将云盘设置为自动续费**



Input: 

```
tccli cbs ModifyDisksRenewFlag --cli-unfold-argument  \
    --DiskIds disk-5w50lrms \
    --RenewFlag NOTIFY_AND_AUTO_RENEW
```

Output: 
```
{
    "Response": {
        "RequestId": "1f01171e-6a0f-4208-bb04-d342d97d42c8"
    }
}
```

