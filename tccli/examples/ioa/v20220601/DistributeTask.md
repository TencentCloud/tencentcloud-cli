**Example 1: 下发任务**

下发任务

Input: 

```
tccli ioa DistributeTask --cli-unfold-argument  \
    --Owner admin \
    --BusinessId 123 \
    --SubId 123 \
    --OsType 0 \
    --Data "{}" \
    --Selects.0.ObjType 1 \
    --Selects.0.Objections 15
```

Output: 
```
{
    "Response": {
        "Data": {
            "Mid": [
                "A021C770C7686FC5601F00B40D93B75560A20D15"
            ],
            "Seq": 26
        },
        "RequestId": "fdb3a312-bf72-43dc-b174-c88375cc395c"
    }
}
```

