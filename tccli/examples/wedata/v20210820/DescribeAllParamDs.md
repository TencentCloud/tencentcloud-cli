**Example 1: 查询所有参数**

查询所有参数

Input: 

```
tccli wedata DescribeAllParamDs --cli-unfold-argument  \
    --ProjectId abc \
    --TaskId abc \
    --WorkflowId abc \
    --OriginalParams abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": 0,
                "ParamKey": "abc",
                "ParamType": "abc",
                "ParamBelong": "abc",
                "ParamDefine": "abc",
                "ParamValue": "abc",
                "ParamOwner": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "Result": true,
                "Msg": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

