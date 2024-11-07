**Example 1: 编辑登录审计白名单**

编辑登录审计白名单

Input: 

```
tccli cwp DescribeLoginWhiteHostList --cli-unfold-argument  \
    --Limit 1 \
    --Id 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Hosts": [
            {
                "MachineName": "机器名称",
                "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "MachineWanIp": "1.1.1.1",
                "Uuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "MachineIp": "1.1.1.1",
                "Tags": [
                    {
                        "Name": "cwp",
                        "TagId": 1,
                        "Rid": 1
                    }
                ]
            }
        ],
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c"
    }
}
```

