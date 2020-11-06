**Example 1: 速算题目批改-同步模式**

同步模式，直接返回结果，TaskId 为空

Input: 

```
tccli hcm Evaluation --cli-unfold-argument  \
    --SessionId stress_test_956938 \
    --Url https%3a%2f%2fhcm-test-1255701415.cos.ap-guangzhou.myqcloud.com%2ffcffd312dfa63b06376d0c6fa34a205c.jpg%3fq-sign-algorithm%3dsha1%26q-ak%3dAKIDtU0Z6XdMq136HtP1NQYS4DEcn3JNEoKs%26q-sign-time%3d1547438152%3b1547439952%26q-key-time%3d1547438152%3b1547439952%26q-header-list%3d%26q-url-param-list%3d%26q-signature%3d779baa6631bc3ceff42c580678bb5866c2591dbe%26x-cos-security-token%3d673ee4f1d5791b6e65ac0efec0b692983cef672210001
```

Output: 
```
{
    "Response": {
        "SessionId": "1112asdfasdf1",
        "Items": [
            {
                "Item": "YES",
                "ItemString": "99+201=300",
                "ItemCoord": {
                    "Height": 181,
                    "Width": 873,
                    "X": 450,
                    "Y": 546
                }
            }
        ],
        "TaskId": "",
        "RequestId": "55ad4928-fa5-415c-2cb-868d5e3171431"
    }
}
```

**Example 2: 速算题目批改-异步模式**

异步模式，只返回 TaskId

Input: 

```
tccli hcm Evaluation --cli-unfold-argument  \
    --SessionId stress_test_956938 \
    --Url xxx \
    --IsAsync 1
```

Output: 
```
{
    "Response": {
        "SessionId": "1112asdfasdf1",
        "Items": null,
        "TaskId": "1000010",
        "RequestId": "55ad4928-fa5-415c-2cb-868d5e3171431"
    }
}
```

