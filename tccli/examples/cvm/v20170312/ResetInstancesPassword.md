**Example 1: 重置一个Linux/Windows实例的密码**

重置一个Linux/Windows实例的密码，之后您可利用此密码登录实例

Input: 

```
tccli cvm ResetInstancesPassword --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy ins-5d8a23rs \
    --Password abc123ABC!@# \
    --ForceStop TRUE
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

