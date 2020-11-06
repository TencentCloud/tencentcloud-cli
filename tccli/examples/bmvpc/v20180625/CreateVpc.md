**Example 1: 创建黑石私有网络**



Input: 

```
tccli bmvpc CreateVpc --cli-unfold-argument  \
    --VpcName test \
    --CidrBlock 10.10.0.0/16 \
    --SubnetSet.0.SubnetName ownDocker1 \
    --SubnetSet.0.CidrBlock 10.10.246.0/26 \
    --SubnetSet.0.Zone ap-test-1 \
    --Zone ap-test
```

Output: 
```
{
    "Response": {
        "TaskId": 1234,
        "RequestId": "09186e64-d19e-4ca1-968f-df4fc8139192"
    }
}
```

