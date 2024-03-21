**Example 1: 修改实例的自动续费开关**



Input: 

```
tccli waf ModifyInstanceRenewFlag --cli-unfold-argument  \
    --InstanceId waf_000000001 \
    --RenewFlag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "b4f13899-561b-46a0-a045-6ba6b72c38f2"
    }
}
```

