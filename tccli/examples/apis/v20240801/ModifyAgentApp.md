**Example 1: 修改app**

修改app

Input: 

```
tccli apis ModifyAgentApp --cli-unfold-argument  \
    --ID aga-71702335 \
    --InstanceID ins-e6fbc9b9 \
    --Name 测试app \
    --Description 测试desp
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "aga-71702335"
        },
        "RequestId": "ccb7929f-710a-4e1a-beff-192ec3f28da0"
    }
}
```

