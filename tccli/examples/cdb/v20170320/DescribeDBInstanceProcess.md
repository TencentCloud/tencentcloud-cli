**Example 1: 查询实例活动线程**

无

Input: 

```
tccli cdb DescribeDBInstanceProcess --cli-unfold-argument  \
    --InstanceId cdb-xdkw92
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Command": "abc",
                "Db": "abc",
                "Id": 1,
                "Info": "abc",
                "State": "abc",
                "Time": 1,
                "User": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

