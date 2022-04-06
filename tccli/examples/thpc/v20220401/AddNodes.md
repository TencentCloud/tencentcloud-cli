**Example 1: 添加节点**



Input: 

```
tccli thpc AddNodes --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ClusterId hpc-52nkfau6 \
    --ImageId img-3la7wgnt \
    --InstanceType S2.SMALL2 \
    --Count 1 \
    --InstanceChargeType SPOTPAID \
    --VirtualPrivateCloud.SubnetId subnet-r0zpktaa \
    --VirtualPrivateCloud.VpcId vpc-r9jw2jzr
```

Output: 
```
{
    "Response": {
        "RequestId": "b2ac2379-6453-4eab-8f63-7ade00cb67b0"
    }
}
```

