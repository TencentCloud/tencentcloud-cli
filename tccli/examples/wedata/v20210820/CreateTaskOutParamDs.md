**Example 1: 创建输出参数**

创建输出参数

Input: 

```
tccli wedata CreateTaskOutParamDs --cli-unfold-argument  \
    --TaskId 20230423161232764 \
    --ParamKey a \
    --ProjectId 123123 \
    --ParamDesc $[0] \
    --ParamDefine $[0]
```

Output: 
```
{
    "Response": {
        "Data": {
            "Success": true,
            "Message": "abc"
        },
        "RequestId": "abc"
    }
}
```

