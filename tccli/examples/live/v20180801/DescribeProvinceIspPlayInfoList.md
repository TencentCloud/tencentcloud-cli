**Example 1: Sample request**

This example shows you how to query the district/ISP [mapping table](https://intl.cloud.tencent.com/document/api/267/34019?from_cn_redirect=1).

Input: 

```
tccli live DescribeProvinceIspPlayInfoList --cli-unfold-argument  \
    --PlayDomains 5000.playdomain.com \
    --StartTime '2019-02-01 00:00:00' \
    --EndTime '2019-02-02 00:00:00' \
    --Granularity 1 \
    --StatType Bandwidth
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Time": "2019-02-01 00:00:00",
                "Value": 500.0
            }
        ],
        "StatType": "Bandwidth",
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

