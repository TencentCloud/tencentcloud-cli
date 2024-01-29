**Example 1: 查询项目全局参数**

查询项目全局参数

Input: 

```
tccli wedata DescribeProjectParamDs --cli-unfold-argument  \
    --ProjectId abc \
    --CurRunDate abc \
    --StartTime abc \
    --KeyWords abc
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

