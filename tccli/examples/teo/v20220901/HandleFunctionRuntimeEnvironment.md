**Example 1: 添加环境变量**

添加指定的环境变量列表到函数运行环境中。

Input: 

```
tccli teo HandleFunctionRuntimeEnvironment --cli-unfold-argument  \
    --ZoneId zone-28569s6od5na \
    --FunctionId ef-22xxf22 \
    --Operation setEnvironmentVariable \
    --EnvironmentVariables.0.Key name \
    --EnvironmentVariables.0.Type string \
    --EnvironmentVariables.0.Value edgeone
```

Output: 
```
{
    "Response": {
        "RequestId": "4dcgtb24-7dc5-46s2-9q3e-95825d53dcs3a"
    }
}
```

**Example 2: 删除环境变量**

删除函数运行环境中的指定环境变量列表。

Input: 

```
tccli teo HandleFunctionRuntimeEnvironment --cli-unfold-argument  \
    --ZoneId zone-28569s6od5na \
    --FunctionId ef-22xxf22 \
    --Operation deleteEnvironmentVariable \
    --EnvironmentVariables.0.Key name \
    --EnvironmentVariables.0.Value 
```

Output: 
```
{
    "Response": {
        "RequestId": "4dcgtb24-7dc5-46s2-9q3e-95825d53dcs3a"
    }
}
```

**Example 3: 清空环境变量**



Input: 

```
tccli teo HandleFunctionRuntimeEnvironment --cli-unfold-argument  \
    --ZoneId zone-28569s6od5na \
    --FunctionId ef-22xxf22 \
    --Operation clearEnvironmentVariable
```

Output: 
```
{
    "Response": {
        "RequestId": "4dcgtb24-7dc5-46s2-9q3e-95825d53dcs3a"
    }
}
```

**Example 4: 重置环境变量**

在函数的运行环境中，使用新的环境变量列表覆盖已有的列表。

Input: 

```
tccli teo HandleFunctionRuntimeEnvironment --cli-unfold-argument  \
    --ZoneId zone-28569s6od5na \
    --FunctionId ef-22xxf22 \
    --Operation resetEnvironmentVariable \
    --EnvironmentVariables.0.Key new_name \
    --EnvironmentVariables.0.Type string \
    --EnvironmentVariables.0.Value edgeone_new
```

Output: 
```
{
    "Response": {
        "RequestId": "4dcgtb24-7dc5-46s2-9q3e-95825d53dcs3a"
    }
}
```

