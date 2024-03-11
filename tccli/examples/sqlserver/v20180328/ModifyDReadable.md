**Example 1: 开通或者关闭备机只读功能**

开通或者关闭备机只读功能

Input: 

```
tccli sqlserver ModifyDReadable --cli-unfold-argument  \
    --InstanceId mssql-j8kv137v \
    --Type enable \
    --VpcId vpc-jh8ah7 \
    --SubnetId sub-i90aoa \
    --Vip 127.0.0.1
```

Output: 
```
{
    "Response": {
        "RequestId": "1fed8472-f117-11ec-be47-525400853186",
        "FlowId": 1012152
    }
}
```

