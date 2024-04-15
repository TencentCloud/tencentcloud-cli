**Example 1: 创建用户自定义函数**



Input: 

```
tccli wedata CreateCustomFunction --cli-unfold-argument  \
    --ProjectId 1470575647377821111 \
    --Type HIVE \
    --Kind OTHER \
    --ClusterIdentifier emr-demo \
    --DbName default \
    --Name demoFu
```

Output: 
```
{
    "Response": {
        "ErrorMessage": null,
        "FunctionId": "217377ce-bcc0-446e-afd9-64ef4b707391",
        "RequestId": "e5ae06d9-898c-48a6-ae27-ed3758d9ef35"
    }
}
```

