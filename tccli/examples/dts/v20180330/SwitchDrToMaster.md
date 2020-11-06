**Example 1: Promoting a disaster recovery instance to a master instance**



Input: 

```
tccli dts SwitchDrToMaster --cli-unfold-argument  \
    --DatabaseType mysql \
    --DstInfo.Region ap-shanghai \
    --DstInfo.InstanceId cdb-mdgezf4d
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "8826bbe9-27ee6768-9bc0a6ae-82962686",
        "RequestId": "0ec651b0-755a-4342-991e-184698c00a31"
    }
}
```

