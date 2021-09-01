**Example 1: 修改实例参数**



Input: 

```
tccli sqlserver ModifyInstanceParam --cli-unfold-argument  \
    --WaitSwitch 0 \
    --InstanceIds mssql-bm5e51kb mssql-p2yli7gv mssql-9ahw2qp9 \
    --ParamList.0.Name 'fill factor(%)' \
    --ParamList.0.CurrentValue 50 \
    --ParamList.1.Name 'cost threshold for parallelism' \
    --ParamList.1.CurrentValue 0
```

Output: 
```
{
    "Response": {
        "RequestId": "74172b7e-139c-4eed-b237-856f56e67f48"
    }
}
```

