**Example 1: 新增实例**



Input: 

```
tccli cynosdb AddInstances --cli-unfold-argument  \
    --Zone ap-guangzhou-3 \
    --VpcId vpc-1ptuei0b \
    --SubnetId subnet-1tmw9t4o \
    --Cpu 2 \
    --Memory 4 \
    --Storage 100 \
    --ClusterId cynosdbmysql-6gtlgm5l \
    --ReadOnlyCount 1 \
    --PayMode 0
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "InstanceId": "cynosdbpg-ins-n8497zx8"
            }
        ],
        "FlowId": 734,
        "RequestId": "ed1bf4b2-4917-4f4f-9f7d-1562e34c9eeb"
    }
}
```

