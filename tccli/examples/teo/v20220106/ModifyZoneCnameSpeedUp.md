**Example 1: 修改 CNAME 加速状态**



Input: 

```
tccli teo ModifyZoneCnameSpeedUp --cli-unfold-argument  \
    --Status xx \
    --Id xx
```

Output: 
```
{
    "Response": {
        "Status": "xx",
        "ModifiedOn": "2020-09-22T00:00:00+00:00",
        "Name": "xx",
        "RequestId": "xx",
        "Id": "xx"
    }
}
```

