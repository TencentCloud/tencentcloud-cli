**Example 1: 任务更新时间**

指定任务更新时间

Input: 

```
tccli ioa DescribeTaskUpdateDate --cli-unfold-argument  \
    --OsType 0 \
    --Mid 718dbbde-7b61-4ba3-80db-b310fb89b9d1
```

Output: 
```
{
    "Response": {
        "Data": {
            "AllLogUpdateTime": "",
            "CheckUpdateTime": "",
            "FileUpdateTime": "",
            "FirstGet": true
        },
        "RequestId": "17450ab2-9c6b-40b5-aae1-613749a3c7fd"
    }
}
```

