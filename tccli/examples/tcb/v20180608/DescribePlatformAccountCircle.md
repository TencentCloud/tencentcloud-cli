**Example 1: 查询平台版资源计费周期**



Input: 

```
tccli tcb DescribePlatformAccountCircle --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EndTime": "2026-09-20 23:59:59",
        "StartTime": "2026-08-20 21:01:24",
        "RequestId": "5552ceb4-5918-46b6-a487-327e035ac538"
    }
}
```

**Example 2: 查询平台版资源计费周期(包含历史周期)**



Input: 

```
tccli tcb DescribePlatformAccountCircle --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EndTime": "2026-09-28 23:59:59",
        "StartTime": "2026-08-29 00:00:00",
        "RequestId": "95410dd7-bfd7-43f4-b228-e0d89f0fab9f"
    }
}
```

