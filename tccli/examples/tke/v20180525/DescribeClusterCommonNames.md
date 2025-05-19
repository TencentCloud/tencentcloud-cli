**Example 1: 获取集群子账户CommonName映射关系**



Input: 

```
tccli tke DescribeClusterCommonNames --cli-unfold-argument  \
    --ClusterId cls-65r1c5nu \
    --SubaccountUins 1311258476067 1311258476067
```

Output: 
```
{
    "Response": {
        "CommonNames": [
            {
                "SubaccountUin": "1311258476067",
                "CN": "1311258476067-1588769189"
            }
        ],
        "RequestId": "33483fde-efec-4d3c-8ff6-340d9dbc2d01"
    }
}
```

