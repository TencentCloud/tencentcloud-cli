**Example 1: 挂起或启动数据引擎**

挂起或启动数据引擎

Input: 

```
tccli dlc SuspendResumeDataEngine --cli-unfold-argument  \
    --DataEngineName abc \
    --Operate suspend
```

Output: 
```
{
    "Response": {
        "DataEngineName": "abc",
        "RequestId": "abc"
    }
}
```

