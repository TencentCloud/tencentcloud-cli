**Example 1: 切换站点状态**



Input: 

```
tccli teo ModifyZoneStatus --cli-unfold-argument  \
    --Paused True \
    --Id xx
```

Output: 
```
{
    "Response": {
        "Paused": true,
        "ModifiedOn": "2020-09-22T00:00:00+00:00",
        "Name": "xx",
        "RequestId": "xx",
        "Id": "xx"
    }
}
```

