**Example 1: 查询用户活动信息**

查询用户活动信息

Input: 

```
tccli tcb DescribeUserActivityInfo --cli-unfold-argument  \
    --ActivityId 1 \
    --ChannelToken ssss \
    --Channel qc_console \
    --GroupId 5d8f5ds45
```

Output: 
```
{
    "Response": {
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351",
        "Tag": "as48sdf45d",
        "Notes": "1,2,3",
        "ActivityTimeLeft": 1,
        "GroupTimeLeft": 1,
        "NickNameList": "a,b,c"
    }
}
```

