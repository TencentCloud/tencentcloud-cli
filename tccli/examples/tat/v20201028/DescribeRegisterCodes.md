**Example 1: 根据Filters查询注册码**

根据Filters查询注册码。

Input: 

```
tccli tat DescribeRegisterCodes --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RegisterCodeSet": [
            {
                "RegisterCodeId": "abc",
                "Description": "abc",
                "InstanceNamePrefix": "abc",
                "RegisterLimit": 0,
                "ExpiredTime": "2020-09-22T00:00:00+00:00",
                "IpAddressRange": "abc",
                "Enabled": true,
                "RegisteredCount": 0,
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "UpdatedTime": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 2: 根据注册码ID查询注册码**

根据注册码ID查询注册码。

Input: 

```
tccli tat DescribeRegisterCodes --cli-unfold-argument  \
    --RegisterCodeIds abc \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RegisterCodeSet": [
            {
                "RegisterCodeId": "abc",
                "Description": "abc",
                "InstanceNamePrefix": "abc",
                "RegisterLimit": 0,
                "ExpiredTime": "2020-09-22T00:00:00+00:00",
                "IpAddressRange": "abc",
                "Enabled": true,
                "RegisteredCount": 0,
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "UpdatedTime": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "abc"
    }
}
```

