**Example 1: 只读组升级为纯网络转发模式**



Input: 

```
tccli cdb UpgradeRoGroup --cli-unfold-argument  \
    --InstanceId cdb-xxx \
    --UniqRoGroupId cdbrg-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "AsyncRequestId": "256117ed-efa08b54-61784d44-91781bbd"
    }
}
```

