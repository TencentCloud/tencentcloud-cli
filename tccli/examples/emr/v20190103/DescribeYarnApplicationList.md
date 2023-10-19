**Example 1: 【监控】查询Yarn作业列表**

查询Yarn作业列表

Input: 

```
tccli emr DescribeYarnApplicationList --cli-unfold-argument  \
    --InstanceId emr-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "Total": 3,
        "YarnApplicationList": [],
        "RequestId": "12345678"
    }
}
```

