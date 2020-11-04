**Example 1: 获取反弹Shell列表**

获取反弹Shell列表

Input: 

```
tccli yunjing DescribeReverseShellEvents --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 12,
        "List": [
            {
                "Id": 12,
                "Uuid": "cf59e3c0-b1cc-11e9-baac-525400ca96ee",
                "Quuid": "b9821ff5-75f0-4939-b21f-13c8d36a725c",
                "Hostip": "10.0.0.125",
                "DstIp": "139.199.79.160",
                "DstPort": 8080,
                "ProcessName": "bash",
                "FullPath": "/bin/bash",
                "CmdLine": "bash -i ",
                "UserName": "root",
                "UserGroup": "root",
                "ParentProcName": "bash",
                "ParentProcUser": "root",
                "ParentProcGroup": "root",
                "ParentProcPath": "/bin/bash",
                "Status": 0,
                "CreateTime": "2019-08-14 19:52:12",
                "MachineName": "云鼎_云镜测试机_Linux_4_weikunlin"
            }
        ],
        "RequestId": "bd9aa8c8-36b6-4991-8e42-d08e80313616"
    }
}
```

