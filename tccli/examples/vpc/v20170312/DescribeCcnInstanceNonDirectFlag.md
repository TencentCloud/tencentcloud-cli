**Example 1: 查看云联网实例非直通标记**



Input: 

```
tccli vpc DescribeCcnInstanceNonDirectFlag --cli-unfold-argument  \
    --BusinessType CFW \
    --CcnId ccn-lwf3h36r \
    --VpcRegion eu-frankfurt \
    --VpcId vpc-ls127qdl
```

Output: 
```
{
    "Response": {
        "NonDirectFlag": false,
        "RequestId": "8fc4cbb5-3dd1-4474-ab81-fb6dbfa330fb"
    }
}
```

