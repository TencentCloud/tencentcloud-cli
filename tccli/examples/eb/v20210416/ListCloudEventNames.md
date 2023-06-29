**Example 1: 查询事件中文名称**

查询事件中文名称

Input: 

```
tccli eb ListCloudEventNames --cli-unfold-argument  \
    --ProductType cvm
```

Output: 
```
{
    "Response": {
        "RequestId": "584caa6b-26d8-4ba5-858d-df1182730075",
        "EventNames": [
            {
                "EventName": "磁盘只读",
                "EventType": "cvm:ErrorEvent:DiskReadonly"
            }
        ]
    }
}
```

