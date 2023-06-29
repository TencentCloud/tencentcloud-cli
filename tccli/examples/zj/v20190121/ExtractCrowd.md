**Example 1: ExtractCrowd**



Input: 

```
tccli zj ExtractCrowd --cli-unfold-argument  \
    --License KA3431QZPU \
    --Id 1234 \
    --Name 人群包名称 \
    --TagList.Age 18 25 \
    --TagList.Gender 1 \
    --TagList.Region c_上海 p_广东 \
    --TagList.Category 服饰 日化 \
    --TagList.PhoneType IPHONE HUAWEI
```

Output: 
```
{
    "Response": {
        "Data": {
            "CrowdID": 47
        },
        "RequestId": "111111"
    }
}
```

