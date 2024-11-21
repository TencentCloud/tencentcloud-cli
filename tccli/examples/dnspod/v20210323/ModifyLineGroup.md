**Example 1: 修改自定义线路分组**

修改自定义线路分组

Input: 

```
tccli dnspod ModifyLineGroup --cli-unfold-argument  \
    --Domain dnspod.cn \
    --Name testgroup99 \
    --Lines 电信,移动 \
    --LineGroupId 10
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166"
    }
}
```

