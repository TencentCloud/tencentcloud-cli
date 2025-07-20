**Example 1: 线路列表**



Input: 

```
tccli igtm DescribeDnsLineList --cli-unfold-argument  \
    --InstanceId gtm-dsdd123xdo
```

Output: 
```
{
    "Response": {
        "DnsLineSet": [
            {
                "DnsLineId": 1,
                "Parent": 1,
                "LineName": "默认",
                "LineId": "1",
                "Useful": true,
                "SubGroup": 1,
                "LinePackage": 1,
                "Weight": 1
            }
        ],
        "RequestId": "8f0325a8-4dd6-4fcb-8f6b-c45e587e51b0"
    }
}
```

