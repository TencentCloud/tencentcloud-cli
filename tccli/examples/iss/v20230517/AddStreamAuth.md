**Example 1: 成功**

 

Input: 

```
tccli iss AddStreamAuth --cli-unfold-argument  \
    --Id 12345678-abcd-efgh-ijkl-1234567890abcd \
    --PullState 0 \
    --PullSecret 123456 \
    --PullExpired 10 \
    --PushState 0 \
    --PushSecret 123456 \
    --PushExpired 10
```

Output: 
```
{
    "Response": {}
}
```

