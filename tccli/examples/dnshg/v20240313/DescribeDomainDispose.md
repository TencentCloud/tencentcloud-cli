**Example 1: 查询封禁记录**

查询封禁记录

Input: 

```
tccli dnshg DescribeDomainDispose --cli-unfold-argument  \
    --CommandId cid-fnkKvSgK1L
```

Output: 
```
{
    "Response": {
        "CommandId": "cid-fnkKvSgK1L",
        "DisposeType": 1,
        "DisposeWay": 3,
        "DomainList": [
            {
                "Area": "1",
                "DisposeTime": null,
                "Domain": "wwww.young49.cn",
                "ForwardIp": null,
                "Reason": "",
                "Status": 1
            }
        ],
        "RequestId": "7f63a160-c3f1-443d-a490-25a5908540f1",
        "TotalCount": 1
    }
}
```

