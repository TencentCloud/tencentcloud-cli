**Example 1: 托管机器移除子网(批量接口)**



Input: 

```
tccli bmvpc DeleteHostedInterfaces --cli-unfold-argument  \
    --InstanceId chm-xxxxxxxx \
    --SubnetIds subnet-xxxxxxxx subnet-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "TaskId": 1234,
        "RequestId": "5383060b-435d-4a54-8201-9e7c2cb5c6ad"
    }
}
```

