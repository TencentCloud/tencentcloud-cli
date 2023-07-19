**Example 1: 批量终止补录计划实例**

批量终止补录计划实例

Input: 

```
tccli wedata KillOpsMakePlanInstances --cli-unfold-argument  \
    --ProjectId 147056160274522xxxx \
    --PlanId e0bed861-0e95-44ca-9d10-28f29752xxxx
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorDesc": null,
            "ErrorId": null,
            "Result": true
        },
        "RequestId": "9d279258-48ed-4be3-84fa-069095c4xxxx"
    }
}
```

