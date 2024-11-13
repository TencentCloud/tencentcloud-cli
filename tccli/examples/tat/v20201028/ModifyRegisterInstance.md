**Example 1: 修改托管实例**

修改托管实例名为"abc"

Input: 

```
tccli tat ModifyRegisterInstance --cli-unfold-argument  \
    --InstanceId rins-xfjkunbgax \
    --InstanceName webserver-01
```

Output: 
```
{
    "Response": {
        "RequestId": "e0f011ac-6949-4726-a7d6-b28540f9d729"
    }
}
```

