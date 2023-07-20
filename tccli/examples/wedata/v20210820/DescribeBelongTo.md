**Example 1: 事件管理-所属任务-基线**

智能运维-事件管理-所属任务/基线

Input: 

```
tccli wedata DescribeBelongTo --cli-unfold-argument  \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

