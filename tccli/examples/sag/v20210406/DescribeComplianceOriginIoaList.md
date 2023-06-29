**Example 1: 获取合规IOA源配置**



Input: 

```
tccli sag DescribeComplianceOriginIoaList --cli-unfold-argument  \
    --Os Windows
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "IoaVersion": "2.4.2"
            }
        ],
        "RequestId": "xxx"
    }
}
```

