**Example 1: 删除自定义函数**

删除自定义函数

Input: 

```
tccli wedata DeleteCustomFunction --cli-unfold-argument  \
    --ProjectId 1470575647377821696 \
    --ClusterIdentifier emr-demo \
    --FunctionId 217377ce-bcc0-446e-afd9-64ef4b707777 \
    --FunctionType HIVE
```

Output: 
```
{
    "Response": {
        "ErrorMessage": null,
        "FunctionId": "217377ce-bcc0-446e-afd9-64ef4b707391",
        "RequestId": "3dfeffd0-74b1-4d5d-bcbd-247de85c9815"
    }
}
```

