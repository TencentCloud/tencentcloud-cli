**Example 1: 描述WAF自动封禁IP 详情**



Input: 

```
tccli waf DescribeAutoDenyIP --cli-unfold-argument  \
    --Count 0 \
    --Category cc \
    --Domain www.test.com \
    --Name name \
    --Ip 192.168.1.1 \
    --VtsMax 1 \
    --VtsMin 1 \
    --Sort CreateTime \
    --Limit 1 \
    --CtsMin 1 \
    --Skip 1 \
    --CtsMax 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Res": [
                {
                    "Action": 32,
                    "Category": "cc",
                    "Ip": "192.168.1.1",
                    "Name": "name",
                    "TsVersion": 1730625888,
                    "ValidTs": 1730625888
                }
            ],
            "TotalCount": 0
        },
        "RequestId": "a4010dd1-d24b-43f5-bab4-8a6b204835b7"
    }
}
```

