**Example 1: 修改云盘自动续费属性**

将云盘disk-5w50lrms设置为自动续费

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

