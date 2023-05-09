**Example 1: ex:**

任何场景

Input: 

```
tccli cynosdb OpenReadOnlyInstanceExclusiveAccess --cli-unfold-argument  \
    --ClusterId cynosdbmysql-qwertyui \
    --InstanceId cynosdbmysql-ins-asdfghjk \
    --VpcId vpc-asdfghjk \
    --SubnetId subnet-qwertyui \
    --Port 3306 \
    --SecurityGroupIds SecurityGroupIds1 SecurityGroupIds2
```

Output: 
```
{
    "Response": {
        "FlowId": "12345",
        "RequestId": "123123123123123"
    }
}
```

