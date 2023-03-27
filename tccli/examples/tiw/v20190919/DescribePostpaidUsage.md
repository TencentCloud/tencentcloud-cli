**Example 1: 查询用户后付费用量**

查询用户后付费用量

Input: 

```
tccli tiw DescribePostpaidUsage --cli-unfold-argument  \
    --BeginTime '2019-12-16 10:44:58' \
    --EndTime '2019-12-16 10:44:58'
```

Output: 
```
{
    "Response": {
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851"
    }
}
```

