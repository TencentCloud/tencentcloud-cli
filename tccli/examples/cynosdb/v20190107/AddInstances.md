**Example 1: 新增实例**



Input: 

```
tccli cynosdb AddInstances --cli-unfold-argument  \
    --ReadOnlyCount 1 \
    --VpcId vpc-1ptuei0b \
    --ClusterId cynosdbmysql-6gtlgm5l \
    --Memory 4 \
    --SubnetId subnet-1tmw9t4o \
    --Cpu 2
```

Output: 
```
{
    "Response": {
        "BigDealIds": [
            "xx"
        ],
        "ResourceIds": [
            "cynosdbpg-ins-n8497zx8"
        ],
        "RequestId": "ed1bf4b2-4917-4f4f-9f7d-1562e34c9eeb",
        "TranId": "xx",
        "DealNames": [
            "xx"
        ]
    }
}
```

