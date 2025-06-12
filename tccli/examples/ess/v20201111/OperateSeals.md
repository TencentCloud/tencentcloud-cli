**Example 1: 启用印章**

将停用的印章修改为启用状态

Input: 

```
tccli ess OperateSeals --cli-unfold-argument  \
    --Operator.UserId yDCAOUUckpycr4l4UuOiTjVB3yTaFaLI \
    --Act 1 \
    --SealIds yDClqUUckpaj38v1UmGrVdB8iMEXjdyR
```

Output: 
```
{
    "Response": {
        "RequestId": "73fd23a3-7e85-48e5-970a-ca50da5e25af"
    }
}
```

