**Example 1: 无**

用户开启实例的透明加密

Input: 

```
tccli dcdb ModifyDBEncryptAttributes --cli-unfold-argument  \
    --InstanceId tdsqlshard-xxx \
    --EncryptEnabled 0
```

Output: 
```
{
    "Response": {
        "RequestId": "afb70c41-025e-4cec-bec3-6207a5d635d6"
    }
}
```

