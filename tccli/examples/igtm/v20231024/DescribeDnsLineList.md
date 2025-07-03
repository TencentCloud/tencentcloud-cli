**Example 1: 线路列表**



Input: 

```
tccli igtm DescribeDnsLineList --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "DnsLineSet": [
            {
                "Parent": 1,
                "LineName": "abc",
                "LineId": "abc",
                "Useful": true,
                "SubGroup": 1,
                "LinePackage": 1,
                "Weight": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

