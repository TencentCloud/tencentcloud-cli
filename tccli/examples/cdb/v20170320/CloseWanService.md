**Example 1: Disabling public network access for instance**



Input: 

```
tccli cdb CloseWanService --cli-unfold-argument  \
    --InstanceId cdb-ezq1vzem
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "AsyncRequestId": "841592f6-dd318344-aea19230-38912726"
    }
}
```

