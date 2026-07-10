**Example 1: 一键开启预设策略**

一键开启预设策略

Input: 

```
tccli monitor EnablePredefinedPolicies --cli-unfold-argument  \
    --PredefinedGroupID qce/cdb \
    --NoticeIDs notice-lnrxepp7
```

Output: 
```
{
    "Response": {
        "RequestId": "79e08710-b7e2-4394-88c3-b00fcbef1bbe"
    }
}
```

