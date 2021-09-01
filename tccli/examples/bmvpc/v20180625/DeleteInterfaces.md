**Example 1: DeleteBmInterfaceBatch**



Input: 

```
tccli bmvpc DeleteInterfaces --cli-unfold-argument  \
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

