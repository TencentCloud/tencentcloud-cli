**Example 1: 添加节点**

往集群ID为hpc-52nkfau6的集群的compute队列增加一个计算节点。

Input: 

```
tccli thpc AddNodes --cli-unfold-argument  \
    --Count 1 \
    --VirtualPrivateCloud.SubnetId subnet-r0zpktaa \
    --VirtualPrivateCloud.VpcId vpc-r9jw2jzr \
    --Placement.Zone ap-guangzhou-2 \
    --ClusterId hpc-52nkfau6 \
    --ImageId img-3la7wgnt \
    --InstanceChargeType SPOTPAID \
    --InstanceType S2.SMALL2 \
    --NodeRole Compute \
    --QueueName compute
```

Output: 
```
{
    "Response": {
        "RequestId": "b2ac2379-6453-4eab-8f63-7ade00cb67b0"
    }
}
```

