**Example 1: 查询某一个账号所有的共享流量包信息**

查询某一个账号所有的共享流量包信息。

Input: 

```
tccli vpc DescribeTrafficPackages --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TrafficPackageSet": [
            {
                "TrafficPackageId": "tfp-g67jlh1j",
                "TrafficPackageName": "未命名",
                "TotalAmount": 10,
                "RemainingAmount": 10,
                "Status": "AVAILABLE",
                "CreatedTime": "2022-08-31T11:42:37Z",
                "Deadline": "2022-09-30T11:42:36Z",
                "DeductType": "FULL_TIME",
                "UsedAmount": 0,
                "TagSet": [
                    {
                        "Key": "aa",
                        "Value": "bb"
                    }
                ]
            }
        ],
        "RequestId": "e92ac36b-db69-4329-b030-9276b88d93c4"
    }
}
```

