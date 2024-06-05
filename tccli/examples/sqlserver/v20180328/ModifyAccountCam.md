**Example 1: 开通CAM鉴权**

存量账户开通CAM鉴权

Input: 

```
tccli sqlserver ModifyAccountCam --cli-unfold-argument  \
    --InstanceId mssql-68iv2kvj \
    --IsCam true \
    --UserName camuser12019
```

Output: 
```
{
    "Response": {
        "RequestId": "0291e1c3-4a2b-4047-9934-8b3f56beff99"
    }
}
```

