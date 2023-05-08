**Example 1: 保存用户自定义函数**



Input: 

```
tccli wedata SaveCustomFunction --cli-unfold-argument  \
    --Kind xx \
    --Description xx \
    --ReturnDesc xx \
    --ParamDesc xx \
    --Example xx \
    --ClassName xx \
    --Usage xx \
    --ResourceList.0.Path xx \
    --ResourceList.0.Id xx \
    --ResourceList.0.Type xx \
    --ResourceList.0.Name xx \
    --ResourceList.0.Md5 xx \
    --ClusterIdentifier xx \
    --FunctionId xx
```

Output: 
```
{
    "Response": {
        "ErrorMessage": "xx",
        "FunctionId": "xx",
        "RequestId": "xx"
    }
}
```

