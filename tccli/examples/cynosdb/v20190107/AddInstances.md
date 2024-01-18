**Example 1: 新增实例**

新增只读实例

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
        "TranId": "abc",
        "DealNames": [
            "abc"
        ],
        "ResourceIds": [
            "abc"
        ],
        "BigDealIds": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

