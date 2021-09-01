**Example 1: 获取高危命令列表**

获取高危命令列表

Input: 

```
tccli yunjing DescribeBashEvents --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "List": [
            {
                "Id": 10,
                "Uuid": "0ba7f086-9d6b-11e9-a431-98be94219792",
                "Quuid": "1a01222b-6ffe-4793-9a9e-4afca2d254ec",
                "Hostip": "10.105.145.42",
                "User": "root",
                "Platform": 4,
                "BashCmd": "ssh root@182.254.203.129",
                "RuleId": 0,
                "RuleName": "",
                "RuleLevel": true,
                "Status": 0,
                "CreateTime": "2019-08-12 10:53:25",
                "MachineName": "云鼎_云镜测试机_Linux_5_weikunlin"
            }
        ],
        "RequestId": "bd9aa8c8-36b6-4991-8e42-d08e80313616"
    }
}
```

