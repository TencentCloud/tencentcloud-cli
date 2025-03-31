**Example 1: 免费版创建**



Input: 

```
tccli vdb CreateInstance --cli-unfold-argument  \
    --VpcId vpc-68mjxcwm \
    --SubnetId subnet-1m1hnqav \
    --PayMode 0 \
    --InstanceName test-base \
    --SecurityGroupIds sg-b85lwctl \
    --InstanceType base
```

Output: 
```
{
    "Response": {
        "InstanceIds": [
            "vdb-j8mv****"
        ],
        "RequestId": "0d7fa142-011a-4416-be8c-320e44c9c3a9"
    }
}
```

