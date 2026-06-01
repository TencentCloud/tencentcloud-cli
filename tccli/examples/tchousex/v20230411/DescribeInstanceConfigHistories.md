**Example 1: 获取集群配置文件修改历史**



Input: 

```
tccli tchousex DescribeInstanceConfigHistories --cli-unfold-argument  \
    --InstanceId abc \
    --Offset 0 \
    --Limit 0 \
    --StartTime abc \
    --EndTime abc \
    --Components abc \
    --FileNames abc \
    --VirtualCluster abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstanceConfigHistories": [
            {
                "FileName": "abc",
                "NewConfValue": "abc",
                "OldConfValue": "abc",
                "Remark": "abc",
                "ModifyTime": "abc",
                "UserUin": "abc"
            }
        ],
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

