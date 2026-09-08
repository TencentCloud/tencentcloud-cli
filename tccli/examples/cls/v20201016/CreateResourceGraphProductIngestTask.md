**Example 1: 接入cdb全部实例**



Input: 

```
tccli cls CreateResourceGraphProductIngestTask --cli-unfold-argument  \
    --ResourceGraphId 649f38d6-3fe9-4412-a31c-ddb701f9e5a9 \
    --Name 产品接入任务-test-5 \
    --CloudProduct cdb \
    --SelectionMode 0
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "TaskId": "2da784dd-1d37-4f98-9950-183b56b735b0",
        "RequestId": "e949cb6d-369f-4a45-b838-078ae3420739"
    }
}
```

