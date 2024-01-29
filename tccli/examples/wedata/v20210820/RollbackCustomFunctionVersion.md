**Example 1: 回滚自定义函数版本**



Input: 

```
tccli wedata RollbackCustomFunctionVersion --cli-unfold-argument  \
    --ClusterIdentifier hive-emr-tersf \
    --Tag test \
    --FunctionId d65df5af-28b4-4171-9a24-ce96fc4e83fa
```

Output: 
```
{
    "Response": {
        "ErrorMessage": "ces",
        "FunctionId": "d65df5af-28b4-4171-9a24-ce96fc4e83fa",
        "RequestId": "4af5a5ed-eb41-4ab7-b1fe-da7b5144eed4"
    }
}
```

