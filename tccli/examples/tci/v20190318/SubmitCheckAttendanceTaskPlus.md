**Example 1: 发起考勤**

发起考勤

Input: 

```
tccli tci SubmitCheckAttendanceTaskPlus --cli-unfold-argument  \
    --FileType vod_url \
    --FileContent http://xxx.mp4 \
    --StartTime 0 \
    --EndTime 0 \
    --LibraryIds library_id
```

Output: 
```
{
    "Response": {
        "RequestId": "21331e8d-4a22-41e3-81c5-50a173962db3",
        "JobId": 549,
        "NotRegisteredSet": null
    }
}
```

