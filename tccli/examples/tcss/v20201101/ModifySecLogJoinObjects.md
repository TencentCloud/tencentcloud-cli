**Example 1: 修改安全日志接入对象**

修改安全日志接入对象

Input: 

```
tccli tcss ModifySecLogJoinObjects --cli-unfold-argument  \
    --NodeType Normal \
    --LogType container_bash \
    --BindList xxxxx xxxxx \
    --UnBindList xxxxx xxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

