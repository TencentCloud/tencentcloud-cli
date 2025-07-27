**Example 1: 克隆实例并回档到指定时间**

克隆实例并回档到指定时间

Input: 

```
tccli cdb CreateCloneInstance --cli-unfold-argument  \
    --UniqVpcId vpc-594gwq4l \
    --InstanceId cdb-9303wd4x \
    --Volume 50 \
    --UniqSubnetId subnet-dz5pj862 \
    --SpecifiedRollbackTime 2020-08-01 16:27:43 \
    --Memory 1000
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

