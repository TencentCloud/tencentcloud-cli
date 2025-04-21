**Example 1: 示例1**

示例1

Input: 

```
tccli ioa DescribeLogDetailLicenseAuthorization --cli-unfold-argument  \
    --Sort.Field @timestamp \
    --Sort.Order desc \
    --StartTime 1726055310 \
    --PageSize 10 \
    --LogId IAMLogin \
    --PageNumber 1 \
    --EndTime 1726141710
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": [],
            "Total": 0
        },
        "RequestId": "76e332a7-3da3-4bf2-acab-0a3aa1d441c2"
    }
}
```

