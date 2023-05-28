**Example 1: 销毁已隔离的TDSQL包年包月实例**

销毁已隔离的TDSQL包年包月实例

Input: 

```
tccli dcdb DestroyDCDBInstance --cli-unfold-argument  \
    --InstanceId tdsqlshard-avw0207d
```

Output: 
```
{
    "Response": {
        "RequestId": "8c4fba95-01e4-61d9-4146-59fc5afdf962",
        "FlowId": 100,
        "InstanceId": "tdsqlshard-avw0207d"
    }
}
```

