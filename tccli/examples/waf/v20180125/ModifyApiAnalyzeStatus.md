**Example 1: api分析页面开关**

api分析页面开关

Input: 

```
tccli waf ModifyApiAnalyzeStatus --cli-unfold-argument  \
    --Status 1 \
    --Domain abc.com
```

Output: 
```
{
    "Response": {
        "Count": 0,
        "UnSupportedList": [
            "abc"
        ],
        "FailDomainList": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

**Example 2: test2**

test2

Input: 

```
tccli waf ModifyApiAnalyzeStatus --cli-unfold-argument  \
    --Status 1 \
    --Domain hzh.qcloud.com
```

Output: 
```
{
    "Response": {
        "Count": 0,
        "UnSupportedList": [
            "abc"
        ],
        "FailDomainList": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

**Example 3: test4**

test2

Input: 

```
tccli waf ModifyApiAnalyzeStatus --cli-unfold-argument  \
    --Status 1 \
    --Domain hzh.qcloud.com
```

Output: 
```
{
    "Response": {
        "Count": 0,
        "UnSupportedList": [
            "abc"
        ],
        "FailDomainList": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

