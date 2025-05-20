**Example 1: 模糊搜索实例摘要信息**

模糊搜索实例摘要信息

Input: 

```
tccli lighthouse SearchInstances --cli-unfold-argument  \
    --Limit 100 \
    --Keyword i
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "InstanceDigestSet": [
            {
                "InstanceId": "lhins-xxxxzzzz",
                "InstanceName": "insxxx",
                "PublicAddresses": [
                    "33.44.55.66"
                ]
            },
            {
                "InstanceId": "lhins-aaaabbbb",
                "InstanceName": "insname",
                "PublicAddresses": [
                    "1.2.1.2"
                ]
            }
        ],
        "RequestId": "cb31e424-0b5f-4f25-8cfc-76121aed5b58"
    }
}
```

