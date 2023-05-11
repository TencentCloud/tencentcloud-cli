**Example 1: 请求示例**

多AZ、单AZ场景下的副本提主

Input: 

```
tccli redis ChangeReplicaToMaster --cli-unfold-argument  \
    --InstanceId crs-sa5**** \
    --GroupId 301524
```

Output: 
```
{
    "Response": {
        "RequestId": "c4ed5948-d156-4931-b9c3-10133a0bb6c9",
        "TaskId": 10856
    }
}
```

