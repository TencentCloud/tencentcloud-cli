**Example 1: demo_2**

示例

Input: 

```
tccli wedata DescribeTaskParamDs --cli-unfold-argument  \
    --TaskId 20230508144306162 \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CreateTime": "2023-06-06 17:08:39",
                "ParamDefine": "wwwww",
                "ParamKey": "test",
                "ParamValue": null,
                "TaskId": "20230508144306162",
                "UpdateTime": "2023-06-06 17:08:39"
            }
        ],
        "RequestId": "ed517293-ce55-4802-9454-1bb582a9a4f4"
    }
}
```

**Example 2: 查询任务引用参数**

查询任务引用参数


Input: 

```
tccli wedata DescribeTaskParamDs --cli-unfold-argument  \
    --TaskId abc \
    --ProjectId 12312321
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TaskId": "abc",
                "ParamKey": "abc",
                "ParamDefine": "abc",
                "ParamValue": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

