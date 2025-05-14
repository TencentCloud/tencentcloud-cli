**Example 1: 修改工作空间实例的续费标识**

修改工作空间实例的续费标识

Input: 

```
tccli thpc ModifyWorkspacesRenewFlag --cli-unfold-argument  \
    --SpaceIds wks-xxxx \
    --RenewFlag NOTIFY_AND_AUTO_RENEW
```

Output: 
```
{
    "Response": {
        "RequestId": "84dea32c-55a7-4a07-b2e9-f7ba4dfaad58"
    }
}
```

