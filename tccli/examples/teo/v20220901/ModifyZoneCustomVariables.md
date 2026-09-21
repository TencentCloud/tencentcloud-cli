**Example 1: 配置站点级自定义变量**

创建站点级自定义变量 user.zone.testa，并配置对应的变量运算规则。

Input: 

```
tccli teo ModifyZoneCustomVariables --cli-unfold-argument  \
    --ZoneId zone-3n1uzjzxffby \
    --CustomVariables.0.Name user.zone.testa \
    --CustomVariables.0.InitialValue ${http.request.headers["key"]} \
    --CustomVariables.0.Description  \
    --CustomVariableOperations.0.Branches.0.Condition ${eo.variable['user.zone.testa']} in ['aBc'] \
    --CustomVariableOperations.0.Branches.0.Actions.0.Name Set \
    --CustomVariableOperations.0.Branches.0.Actions.0.SetParameters.Name user.zone.testa \
    --CustomVariableOperations.0.Branches.0.Actions.0.SetParameters.Value ${http.request.host}
```

Output: 
```
{
    "Response": {
        "RequestId": "a33d2e57-25db-43de-add9-cf43748af91c"
    }
}
```

