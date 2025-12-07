**Example 1: 关闭云联网实例非直通标记**



Input: 

```
tccli vpc DisableCcnInstanceNonDirectFlag --cli-unfold-argument  \
    --BusinessType CFW \
    --CcnId ccn-2t2bneq1 \
    --VpcRegion ap-guangzhou \
    --VpcId vpc-293oax59
```

Output: 
```
{
    "Response": {
        "RequestId": "fd58c581-9257-4ccb-a452-25b0794d93d2"
    }
}
```

