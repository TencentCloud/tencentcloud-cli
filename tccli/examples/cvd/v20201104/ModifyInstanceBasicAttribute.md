**Example 1: ModifyInstanceBasicAttribute**



Input: 

```
tccli cvd ModifyInstanceBasicAttribute --cli-unfold-argument  \
    --InstanceId cdi-a \
    --AttributeInfoList.0.Name Name \
    --AttributeInfoList.0.Value new_name
```

Output: 
```
{
    "Response": {
        "RequestId": "rid"
    }
}
```

