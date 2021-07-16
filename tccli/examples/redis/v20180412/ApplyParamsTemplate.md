**Example 1: 修改实例参数**



Input: 

```
tccli redis ApplyParamsTemplate --cli-unfold-argument  \
    --InstanceIds crs-5a4py64p \
    --TemplateId crs-cfg-rhlppeye
```

Output: 
```
{
    "Response": {
        "TaskIds": [
            212,
            213,
            214
        ],
        "RequestId": "e546784b-709c-401d-aba6-73037eb4e522"
    }
}
```

