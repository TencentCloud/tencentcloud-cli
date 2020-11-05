**Example 1: Re-applying for instance association**



Input: 

```
tccli vpc ResetAttachCcnInstances --cli-unfold-argument  \
    --CcnId ccn-gree226l\
    --CcnUin 979137\
    --Instances.0.InstanceType VPC\
    --Instances.0.InstanceId vpc-3dr1zrr9\
    --Instances.0.InstanceRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "627c2362-890f-4f9e-9158-5e457b80d48b"
    }
}
```

