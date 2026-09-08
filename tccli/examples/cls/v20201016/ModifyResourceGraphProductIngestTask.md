**Example 1: 修改cdb接入任务实例选择方式**



Input: 

```
tccli cls ModifyResourceGraphProductIngestTask --cli-unfold-argument  \
    --ResourceGraphId 649f38d6-3fe9-4412-a31c-ddb701f9e5a9 \
    --TaskId 364f5096-24a1-4d0f-915d-330968625671 \
    --SelectionMode 2 \
    --InstanceIds cdb-asdl12x
```

Output: 
```
{
    "Response": {
        "RequestId": "31d08cd7-ec23-476e-9e4d-8d256e228886"
    }
}
```

